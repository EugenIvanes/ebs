# Generated by Django 3.1.14 on 2022-03-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apishop', '0002_auto_20220309_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(upload_to='static/image/'),
        ),
    ]