# Generated by Django 3.1.14 on 2022-03-10 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubsshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='comlete',
            new_name='complete',
        ),
    ]
