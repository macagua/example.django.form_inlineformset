# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(verbose_name='Recipe', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='number',
            field=models.PositiveSmallIntegerField(help_text='Step number', verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='recipe',
            field=models.ForeignKey(verbose_name='Recipe', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
