# Generated by Django 2.1.1 on 2019-06-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
                ('draft', models.BooleanField(default=False)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('read_time', models.TimeField(blank=True, null=True)),
                ('is_doing', models.BooleanField(default=False)),
                ('assignee_id', models.CharField(blank=True, max_length=120)),
                ('progress_percent', models.IntegerField(default=0)),
                ('default_cost', models.FloatField(null=True)),
                ('actual_cost', models.FloatField(null=True)),
                ('done_time', models.FloatField(null=True)),
            ],
        ),
    ]
