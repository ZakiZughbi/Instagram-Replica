# Generated by Django 2.2.2 on 2019-06-12 15:28

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190612_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics', verbose_name=django.contrib.auth.models.User),
        ),
    ]
