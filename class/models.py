from django.db import models

class Subject(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=300)
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.id}  {self.name}'