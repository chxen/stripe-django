from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
