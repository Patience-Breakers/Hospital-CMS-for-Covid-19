# Generated by Django 3.1.3 on 2020-12-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201229_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Covid_test',
            field=models.CharField(default='', max_length=500),
        ),
    ]
