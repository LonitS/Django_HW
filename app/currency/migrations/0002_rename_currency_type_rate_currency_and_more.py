# Generated by Django 4.2.2 on 2023-07-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='currency_type',
            new_name='currency',
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]