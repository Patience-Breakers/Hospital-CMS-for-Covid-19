# Generated by Django 3.1.3 on 2021-01-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20210123_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='recovered',
            field=models.BooleanField(default=False),
        ),
    ]
