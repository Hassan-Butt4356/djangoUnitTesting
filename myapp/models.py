from django.db import models

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=255)
    price=models.PositiveIntegerField(default=0)
    detail=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title