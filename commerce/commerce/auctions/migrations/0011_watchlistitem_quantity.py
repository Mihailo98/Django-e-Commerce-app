# Generated by Django 4.0.4 on 2022-06-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_watchlist_al_watchlistitem_watchlist_als'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlistitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
