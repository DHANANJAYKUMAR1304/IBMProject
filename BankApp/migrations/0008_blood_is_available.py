# Generated by Django 3.2.5 on 2021-07-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankApp', '0007_auto_20210731_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]