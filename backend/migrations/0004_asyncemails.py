# Generated by Django 2.1.7 on 2019-02-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190227_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsyncEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sent_time', models.DateTimeField()),
                ('sent', models.BooleanField(default=False)),
                ('to_name', models.CharField(max_length=255)),
                ('to_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('msg_txt', models.TextField()),
                ('from_name', models.CharField(blank=True, max_length=255, null=True)),
                ('from_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
