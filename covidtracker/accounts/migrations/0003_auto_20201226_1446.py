# Generated by Django 3.1.3 on 2020-12-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_doctor_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.TextField(max_length=1000),
        ),
    ]