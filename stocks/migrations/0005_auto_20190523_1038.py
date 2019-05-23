# Generated by Django 2.1.1 on 2019-05-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_stock_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='EPS',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ROE',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='RSI_14',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='RSI_14_diff',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='market_capitalization',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.FloatField(null=True),
        ),
    ]
