# Generated by Django 3.1.3 on 2021-01-26 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_remove_itemstotalcount_cotton_in_kg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemstotalcount',
            old_name='gloves',
            new_name='vaccines',
        ),
    ]