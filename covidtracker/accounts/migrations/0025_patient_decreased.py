# Generated by Django 3.1.3 on 2020-12-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_itemstotalcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='decreased',
            field=models.BooleanField(default=False),
        ),
    ]
