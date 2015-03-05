# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations, transaction
import django.utils.timezone

# the function that will be used by the migration operation
@transaction.atomic
def copy_old_users(apps, schema_editor):
    # the default user class
    User = apps.get_model("auth", "User")
    # my custom user class
    MyUser = apps.get_model("note", "MyUser")

    # the fields I want to copy from User to MyUser
    fields = ['id', 'username', 'email', 'first_name', 'last_name',
              'is_staff', 'is_active', 'date_joined', 'is_superuser',
              'last_login']

    # for loop to copy all users from one class to the other
    for user in User.objects.all():
        custom_user = MyUser()
        for field in fields:
            setattr(custom_user, field, getattr(user, field))

        custom_user.save()

        # also, groups and permissions should be copied
        custom_user.groups.add(*user.groups.all())
        custom_user.user_permissions.add(*user.user_permissions.all())


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20150305_0955'),
    ]

    operations = [
        migrations.RunPython(copy_old_users)
    ]
