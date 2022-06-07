from django.contrib import admin

from auctions.models import Auction_listings, Bids, Category, Comments, User, Watchlist, WatchlistItem

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_listings)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Watchlist)
admin.site.register(WatchlistItem)