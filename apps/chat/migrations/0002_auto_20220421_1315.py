# Generated by Django 3.2.12 on 2022-04-21 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messenger',
            name='sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='messenger',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_msg', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messenger',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_msg', to=settings.AUTH_USER_MODEL),
        ),
    ]