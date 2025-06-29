# Generated by Django 5.2.2 on 2025-06-08 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_movie_allow_download_movie_download_url_movie_share_enabled'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='allow_download',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='download_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_genres',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='share_enabled',
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='in_watchlists', to='core.movie'),
        ),
    ]
