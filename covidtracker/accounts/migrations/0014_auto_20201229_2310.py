# Generated by Django 3.1.3 on 2020-12-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201229_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]