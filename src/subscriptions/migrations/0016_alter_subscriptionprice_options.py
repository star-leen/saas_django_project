# Generated by Django 5.0.7 on 2024-07-27 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_alter_subscription_options_subscription_featured_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptionprice',
            options={'ordering': ['subscription__order', 'order', 'featured', '-updated']},
        ),
    ]
