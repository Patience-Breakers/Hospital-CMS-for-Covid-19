# Generated by Django 3.1.3 on 2021-01-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210120_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('O', 'Others')], default='M', max_length=2, null=True),
        ),
    ]
