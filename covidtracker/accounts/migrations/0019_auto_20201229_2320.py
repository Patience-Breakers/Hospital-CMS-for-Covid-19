# Generated by Django 3.1.3 on 2020-12-29 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20201229_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='health_status',
            new_name='covid_test_result',
        ),
    ]
