# Generated by Django 4.0.6 on 2022-07-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookloan', '0002_alter_bookloan_borrow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookloan',
            name='borrow_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
