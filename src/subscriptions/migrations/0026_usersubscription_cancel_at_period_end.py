# Generated by Django 5.0.7 on 2024-08-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0025_usersubscription_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
    ]
