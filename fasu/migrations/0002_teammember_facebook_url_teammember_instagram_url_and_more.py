# Generated by Django 5.0.6 on 2024-11-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]