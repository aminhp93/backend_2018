# Generated by Django 2.1.1 on 2019-05-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='financial_data',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_data',
            field=models.TextField(null=True),
        ),
    ]