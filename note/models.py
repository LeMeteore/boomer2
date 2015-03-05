from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Note(models.Model):
    # always reference the User class using setting conf
    author = models.ForeignKey(User)
    value = models.IntegerField(max_length=255)
    def __str__(self):
        return "your note is %s" % self.value
