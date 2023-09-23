from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Range(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Borne(models.Model):
    range = models.ForeignKey(Range, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(default="Default description")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='path/to/upload/', null=True, blank=True)
    # Add any other fields that might be relevant, e.g., specifications, features, etc.

    def __str__(self):
        return self.name
