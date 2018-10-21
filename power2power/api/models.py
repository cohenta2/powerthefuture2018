from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    eth_address = models.CharField(max_length=255)


class Node(models.Model):
    flow = models.IntegerField(default=0)
    neighbor_ids = models.ManyToManyField('self', symmetrical=False, related_name='neighbor')
    cost_per_unit = models.PositiveIntegerField(default=1)
    balance = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
