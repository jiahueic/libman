# Generated by Django 4.0.6 on 2022-07-20 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_issued_retured_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='borrow_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='issued_retured_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='student',
        ),
    ]
