# Generated by Django 3.1.3 on 2021-01-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20210121_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(max_length=500),
        ),
    ]
