from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(blank=True, null=True, max_length=225)
    status = models.CharField(blank=True, null=True, max_length=225)
    created_at = models.DateTimeField(auto_now=True)

