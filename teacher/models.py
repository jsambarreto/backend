from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length = 100, null=False, blank=False)
    value = models.DecimalField(max_digits = 9, decimal_places=2, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.URLField(max_length = 255, null=False, blank=False)


class Aula(models.Model):
    name = models.CharField(max_length = 100, null=False, blank=False)
    email = models.EmailField(max_length = 255, null=False, blank=False)
    professor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name="aulas", null=False, blank=False)