from django.db import models

# Create your models here.

class employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=200)
    emp_designation = models.CharField(max_length=200)
    emp_doj = models.DateField()

    class Meta:
        db_table = "employee"