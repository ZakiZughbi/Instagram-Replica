# Generated by Django 2.1.7 on 2019-02-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_auto_20190225_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default-post.png', upload_to='profile_pics'),
        ),
    ]
