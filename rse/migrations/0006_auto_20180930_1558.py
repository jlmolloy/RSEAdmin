# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-30 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rse', '0005_auto_20180930_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarygradechange',
            name='salary_band',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='rse.SalaryBand'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salarygradechange',
            name='rse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rse.RSE'),
        ),
    ]