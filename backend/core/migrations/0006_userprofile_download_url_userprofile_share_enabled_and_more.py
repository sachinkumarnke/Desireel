# Generated by Django 5.0.2 on 2025-06-07 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_userprofile_allow_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='download_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='share_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='StreamingContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streaming_url', models.URLField(help_text='URL for streaming the movie')),
                ('download_url', models.URLField(blank=True, help_text='URL for downloading the movie', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streaming_content', to='core.movie')),
            ],
        ),
    ]
