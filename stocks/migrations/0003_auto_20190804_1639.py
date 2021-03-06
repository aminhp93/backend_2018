# Generated by Django 2.1.1 on 2019-08-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20190804_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='date',
        ),
        migrations.AddField(
            model_name='stock',
            name='Date',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='High',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='Low',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='Open',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='Value',
            field=models.FloatField(null=True),
        ),
    ]
