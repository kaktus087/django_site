# Generated by Django 3.0.5 on 2020-06-11 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200611_0335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
