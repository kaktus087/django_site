# Generated by Django 3.0.5 on 2020-06-11 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_messages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]