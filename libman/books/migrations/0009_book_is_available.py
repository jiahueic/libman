# Generated by Django 4.0.6 on 2022-07-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
