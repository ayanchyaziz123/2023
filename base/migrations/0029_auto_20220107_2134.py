# Generated by Django 3.1.4 on 2022-01-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_remove_productpricehistory_countinstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpricehistory',
            name='createdAt',
            field=models.DateField(auto_now=True),
        ),
    ]
