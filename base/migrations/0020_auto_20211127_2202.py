# Generated by Django 3.1.4 on 2021-11-27 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0019_couponredemption_is_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couponredemption',
            old_name='is_used',
            new_name='status',
        ),
        migrations.CreateModel(
            name='SubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(blank=True, default=0, null=True)),
                ('filtering_history', models.CharField(blank=True, max_length=400, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
