from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.national_code}"
