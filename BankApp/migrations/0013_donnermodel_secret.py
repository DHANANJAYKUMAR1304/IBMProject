# Generated by Django 3.2.5 on 2021-08-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankApp', '0012_auto_20210817_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnermodel',
            name='Secret',
            field=models.CharField(default='SGN1ONS', max_length=100),
        ),
    ]
