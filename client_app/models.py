from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
