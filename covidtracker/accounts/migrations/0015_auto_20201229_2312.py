# Generated by Django 3.1.3 on 2020-12-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20201229_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
