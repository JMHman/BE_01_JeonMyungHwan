# Generated by Django 5.0.2 on 2024-03-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_review_content_remove_review_likes_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=1231),
            preserve_default=False,
        ),
    ]