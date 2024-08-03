# Generated by Django 5.0.7 on 2024-07-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0021_alter_subscription_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['order', 'featured', '-updated'], 'permissions': [('advanced', 'Advanced Perm'), ('tack', 'Tack Perm'), ('basic', 'Basic Perm')]},
        ),
        migrations.AlterField(
            model_name='subscription',
            name='permissions',
            field=models.ManyToManyField(limit_choices_to={'codename__in': ['advanced', 'tack', 'basic'], 'content_type__app_label': 'subscriptions'}, to='auth.permission'),
        ),
    ]
