# Generated by Django 4.2.4 on 2023-10-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartmodel_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='payout',
            field=models.BooleanField(default=False),
        ),
    ]
