# Generated by Django 3.1.7 on 2021-04-15 07:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_booksmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]