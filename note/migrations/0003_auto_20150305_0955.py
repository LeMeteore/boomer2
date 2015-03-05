# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_myuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AddField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(verbose_name='email address', max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='dany', max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username'),
            preserve_default=False,
        ),
    ]
