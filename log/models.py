from django.db import models
from student.models import Student

class Log(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    math= models.DecimalField(max_digits=5, decimal_places=2)
    physic = models.DecimalField(max_digits=5, decimal_places=2)
    chemistry = models.DecimalField(max_digits=5, decimal_places=2)
    farsi = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report Card for {self.student.name} {self.student.last_name}"


