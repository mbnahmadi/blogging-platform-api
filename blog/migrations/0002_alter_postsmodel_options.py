# Generated by Django 5.1.2 on 2025-01-22 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postsmodel',
            options={'verbose_name_plural': 'blog'},
        ),
    ]
