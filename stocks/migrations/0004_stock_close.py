# Generated by Django 2.1.1 on 2019-05-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20190523_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='close',
            field=models.TextField(null=True),
        ),
    ]