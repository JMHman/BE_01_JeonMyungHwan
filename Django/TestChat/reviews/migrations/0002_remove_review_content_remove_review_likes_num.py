# Generated by Django 5.0.2 on 2024-03-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='likes_num',
        ),
    ]
