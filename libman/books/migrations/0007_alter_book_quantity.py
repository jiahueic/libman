# Generated by Django 4.0.6 on 2022-07-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]