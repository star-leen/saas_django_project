# Generated by Django 5.0.7 on 2024-07-27 00:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_alter_subscriptionprice_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['order', 'featured', '-updated'], 'permissions': [('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm')]},
        ),
        migrations.AddField(
            model_name='subscription',
            name='featured',
            field=models.BooleanField(default=True, help_text='Featured on django pricing page'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='order',
            field=models.IntegerField(default=-1, help_text='Ordering on django price page'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
