# Generated by Django 5.0.7 on 2024-07-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='groups',
            field=models.ManyToManyField(to='auth.group'),
        ),
    ]
