# Generated by Django 3.2.12 on 2022-05-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uid',
            field=models.CharField(blank=True, max_length=500, verbose_name='code post'),
        ),
    ]
