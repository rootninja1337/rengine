# Generated by Django 3.0.6 on 2020-05-16 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scannedsubdomains',
            old_name='scan_history_model',
            new_name='scan_history',
        ),
    ]
