# Generated by Django 3.0.6 on 2020-05-29 15:48

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('post_by_author', django.db.models.manager.Manager()),
            ],
        ),
    ]
