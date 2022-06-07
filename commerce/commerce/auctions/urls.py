from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create', views.create_listing, name='create'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('add_to_watchlist/<int:listing_id>', views.add_to_watchlist, name='watchlist'),
    path('remove_from_watchlist/<int:listing_id>', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('watchlist/', views.WatchlistView.as_view(), name='watchlist_page')
]
