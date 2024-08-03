# Generated by Django 5.0.7 on 2024-07-27 00:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0012_subscriptionprice_featured_subscriptionprice_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionprice',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptionprice',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subscriptionprice',
            name='featured',
            field=models.BooleanField(default=True, help_text='Featured on django pricing page'),
        ),
        migrations.AlterField(
            model_name='subscriptionprice',
            name='order',
            field=models.IntegerField(default=-1, help_text='Ordering on django price page'),
        ),
    ]
