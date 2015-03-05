from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, Permission, Group

# Create your models here.
class Note(models.Model):
    # always reference the User class using setting conf
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    value = models.IntegerField(max_length=255)
    def __str__(self):
        return "your note is %s" % self.value

# I was obliged to create MyPermissionsMixin class
# to avoid the clash with the default PermissionsMixin class
# And I have renamed the related_name used
class MyPermissionsMixin(models.Model):
    """
    A mixin class that adds the fields and methods necessary to support
    Django's Group and Permission model using the ModelBackend.
    """
    is_superuser = models.BooleanField(_('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))
    groups = models.ManyToManyField(Group, verbose_name=_('groups'),
        blank=True, help_text=_('The groups this user belongs to. A user will '
                                'get all permissions granted to each of '
                                'his/her group.'),
        related_name="myuser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission,
        verbose_name=_('user permissions'), blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="myuser_set", related_query_name="user")

    class Meta:
        abstract = True

    def get_group_permissions(self, obj=None):
        """
        Returns a list of permission strings that this user has through their
        groups. This method queries all available auth backends. If an object
        is passed in, only permissions matching this object are returned.
        """
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions

    def get_all_permissions(self, obj=None):
        return _user_get_all_permissions(self, obj)

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission. This method
        queries all available auth backends, but returns immediately if any
        backend returns True. Thus, a user who has permission from a single
        auth backend is assumed to have permission in general. If an object is
        provided, permissions for this specific object are checked.
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)



# I have extended AbstractBaseUser because,
# extending AbstractUser resulted in clashes about groups and permissions
# this custom User class is not yet complete
# this custom User class is not yet the default used by django.
class MyUser(AbstractBaseUser, MyPermissionsMixin):
    is_devops = True
