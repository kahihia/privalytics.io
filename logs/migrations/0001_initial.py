# Generated by Django 2.1.5 on 2019-02-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTypeSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account_type', models.IntegerField(blank=True, choices=[(1, 'basic'), (2, 'advanced')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeToStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('measured_time', models.FloatField()),
                ('measured_type', models.IntegerField(choices=[(1, 'post_time'), (2, 'make_dashboard')], default=1)),
            ],
        ),
    ]