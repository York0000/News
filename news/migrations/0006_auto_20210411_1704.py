# Generated by Django 3.1.7 on 2021-04-11 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210411_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booksmodel',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
