# Generated by Django 3.2.12 on 2022-05-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('date_added',)},
        ),
    ]
