# Generated by Django 4.0.4 on 2022-06-07 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_watchlistitem_al'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='al',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auctions.auction_listings'),
        ),
    ]
