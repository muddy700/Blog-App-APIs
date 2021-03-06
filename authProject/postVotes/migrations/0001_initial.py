# Generated by Django 3.2 on 2021-04-13 11:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('down', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('userIds', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('users', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, size=None)),
                ('up_vote', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, size=None)),
                ('down_vote', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, size=None)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
