# Generated by Django 5.0.7 on 2024-07-27 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_alter_subscriptionprice_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='features',
            field=models.TextField(blank=True, help_text='Features for pricing. Seperated by new line', null=True),
        ),
    ]