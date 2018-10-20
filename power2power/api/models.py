from django.db import models

# Create your models here.

class Node(models.Model):
    power_in = models.PositiveIntegerField()
    power_out = models.PositiveIntegerField()
    enabled = models.BooleanField(default=False)
    neighbor_ids = models.ManyToManyField('self', symmetrical=False, related_name='neighbor')
    surge_multiplier = models.PositiveIntegerField(default=1)
    base_cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2, default=0.10)


    @property
    def total_cost(self):
        return self.surge_multiplier * base_cost_per_unit

    def __str__(self):
        return self.id
