from audioop import reverse
from distutils.command.upload import upload
from keyword import kwlist
from django.contrib.auth.models import AbstractUser
from django.db import models
from pkg_resources import require

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=3000)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"Username: {self.username}, E-mail: {self.email}"

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f"{self.name}"

class Auction_listings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=100)
    photo = models.ImageField()
    price = models.CharField(max_length=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self) -> str:
        return f"{self.title}, Description: {self.description}, price: {self.price}, Category: {self.category}"    

class WatchlistItem(models.Model):
    id = models.AutoField(primary_key=True)
    al = models.ForeignKey(Auction_listings, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.al.title}"

class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    als = models.ManyToManyField(WatchlistItem)

    def __str__(self) -> str:
        return f"{self.als}"


class Bids(models.Model):
    id = models.AutoField(primary_key=True)
    pass

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    pass

