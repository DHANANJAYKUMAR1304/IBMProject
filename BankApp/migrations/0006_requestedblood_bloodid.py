# Generated by Django 3.2.5 on 2021-07-31 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankApp', '0005_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedblood',
            name='Bloodid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BankApp.blood'),
            preserve_default=False,
        ),
    ]
