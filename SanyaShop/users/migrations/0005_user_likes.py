# Generated by Django 3.1.4 on 2020-12-17 22:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
