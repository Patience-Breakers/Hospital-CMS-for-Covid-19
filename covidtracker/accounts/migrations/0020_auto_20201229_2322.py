# Generated by Django 3.1.3 on 2020-12-29 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20201229_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='doctor_id',
            new_name='doctor',
        ),
    ]
