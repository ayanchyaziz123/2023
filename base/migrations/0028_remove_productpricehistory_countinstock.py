# Generated by Django 3.1.4 on 2022-01-07 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_productpricehistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpricehistory',
            name='countInStock',
        ),
    ]