# Generated by Django 3.1.3 on 2020-12-30 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20201229_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
    ]