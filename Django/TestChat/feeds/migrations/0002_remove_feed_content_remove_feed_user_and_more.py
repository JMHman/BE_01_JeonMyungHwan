# Generated by Django 5.0.2 on 2024-03-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='content',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='user',
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(default='users.User', max_length=30),
        ),
    ]
