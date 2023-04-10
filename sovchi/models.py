from django.db import models

# Create your models here.
class Sovchi(models.Model):
    GENDER = (
        ('e','erkak'),
        ('a','ayol'),
    )
    # STUDY = (
    #     ('COLLEGE','COLLEGE'),
    #     ('Institute', 'Institute'),
    # )
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    age = models.IntegerField(default=18)
    cell_phone = models.IntegerField()
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to='images/',blank=True)
    hobby = models.TextField()
    study = models.CharField(max_length=255)
    work_salary = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=15)
    def __str__(self):
        return self.full_name
