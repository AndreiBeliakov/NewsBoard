# Generated by Django 4.1.1 on 2022-10-07 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_remove_post_categories_post_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]