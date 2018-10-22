# Generated by Django 2.1.1 on 2018-10-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=120)),
                ('Close', models.DecimalField(decimal_places=16, max_digits=30, null=True)),
                ('Open', models.DecimalField(decimal_places=16, max_digits=30, null=True)),
                ('High', models.DecimalField(decimal_places=16, max_digits=30, null=True)),
                ('Low', models.DecimalField(decimal_places=16, max_digits=30, null=True)),
                ('Volume', models.DecimalField(decimal_places=16, max_digits=30, null=True)),
                ('Value', models.DecimalField(decimal_places=16, max_digits=30, null=True)),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]