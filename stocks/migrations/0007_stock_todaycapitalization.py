# Generated by Django 2.1.1 on 2019-05-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_auto_20190523_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='TodayCapitalization',
            field=models.FloatField(null=True),
        ),
    ]