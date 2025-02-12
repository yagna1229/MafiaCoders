from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    EventName = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name
    