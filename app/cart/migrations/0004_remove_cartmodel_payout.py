# Generated by Django 4.2.4 on 2023-10-03 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartmodel_payout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='payout',
        ),
    ]
