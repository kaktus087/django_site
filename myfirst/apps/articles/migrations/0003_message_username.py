# Generated by Django 3.0.5 on 2020-06-11 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_remove_message_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор сообщения'),
            preserve_default=False,
        ),
    ]
