# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-02 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_project', '0003_auto_20180131_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verify_email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_project.Login')),
            ],
        ),
    ]
