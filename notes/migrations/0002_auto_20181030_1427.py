# Generated by Django 2.1.1 on 2018-10-30 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note',
            new_name='content',
        ),
    ]
