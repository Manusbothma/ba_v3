# Generated by Django 4.2.4 on 2023-08-23 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_service_short_decription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='short_decription',
            new_name='service_content',
        ),
    ]