from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    eth_address = models.CharField(max_length=255)


class Node(models.Model):
    power_in = models.PositiveIntegerField()
    power_out = models.PositiveIntegerField()
    enabled = models.BooleanField(default=False)
    neighbor_ids = models.ManyToManyField('self', symmetrical=False, related_name='neighbor')
    surge_multiplier = models.PositiveIntegerField(default=1)
    base_cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2, default=0.10)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @property
    def total_cost(self):
        return self.surge_multiplier * base_cost_per_unit
