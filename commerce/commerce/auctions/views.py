from django.contrib import messages
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, View

from auctions.functions import handle_uploaded_file

from .models import Auction_listings, Category, User, Watchlist, WatchlistItem

class CreateListingForm(ModelForm):
    class Meta:
        model = Auction_listings
        fields = '__all__'

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "auctions/index.html", {
        'listings': Auction_listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == 'POST':
        f = CreateListingForm(request.POST, request.FILES)
        if f.is_valid():
            handle_uploaded_file(request.FILES['photo'])
            f.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'auctions/create_listing.html', {
                'createForm': f
        })
    return render(request, 'auctions/create_listing.html', {
        'createForm': CreateListingForm()
    })

def listing(request, listing_id):
    l = Auction_listings.objects.get(id=listing_id)
    return render(request, "auctions/listing.html", {
        'listing': l
    })

def add_to_watchlist(request, listing_id):
    listing = get_object_or_404(Auction_listings, id=listing_id)
    watchlist_item, create = WatchlistItem.objects.get_or_create(al=listing)
    watchlist_item.quantity += 1
    watchlist_item.save()
    wl = Watchlist.objects.create()
    wl.als.add(watchlist_item)
    messages.add_message(request, messages.INFO, 'This listing was added to watchlist.')
    return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
    
def remove_from_watchlist(request, listing_id):
    listing = get_object_or_404(Auction_listings, id=listing_id)
    wli = WatchlistItem.objects.get(al=listing)
    wli.al.delete()
    return HttpResponseRedirect(reverse('watchlist_page'))

class WatchlistView(View):
    def get(self, *args, **kwargs):
        wli = WatchlistItem.objects.all()
        return render(self.request, 'auctions/watchlist.html', {
            'object': wli
        })