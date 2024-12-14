from django.db import models

class CarData(models.Model):
  id = models.AutoField(primary_key=True)
  model = models.CharField(max_length=64)
  year = models.IntegerField()

  def __str__(self):
    return super().__str__(f"{self.id} {self.model} {self.year}")
