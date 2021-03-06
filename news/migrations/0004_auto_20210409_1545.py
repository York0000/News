# Generated by Django 3.1.7 on 2021-04-09 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210407_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.categorymodel'),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='page_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
