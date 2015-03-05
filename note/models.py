from django.db import models
from django.conf import settings

# Create your models here.
# Create your models here.
class Note(models.Model):
    # always reference the User class using setting conf
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    value = models.IntegerField(max_length=255)
    def __str__(self):
        return "your note is %s" % self.value
