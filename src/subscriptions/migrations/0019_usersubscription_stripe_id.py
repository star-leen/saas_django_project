# Generated by Django 5.0.7 on 2024-07-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0018_subscription_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
