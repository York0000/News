# Generated by Django 3.1.7 on 2021-04-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210409_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]