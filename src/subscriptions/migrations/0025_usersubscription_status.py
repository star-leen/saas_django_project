# Generated by Django 5.0.7 on 2024-08-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0024_usersubscription_current_period_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('trailing', 'Trailing'), ('incomplete', 'Incomplete'), ('incomplete_expired', 'Incomplete_Expired'), ('past_due', 'Past_Due'), ('canceled', 'Canceled'), ('unpaid', 'Unpaid'), ('paused', 'Paused')], max_length=20, null=True),
        ),
    ]