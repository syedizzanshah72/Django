from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    Chai_Type_Choice = [
        ('ML','MASALA'),
        ('GR','Ginger'),
        ('kI','KIWI')
    ]
    name = models.CharField(max_length=120)
    message = models.TextField(max_length=1000)
    type = models.CharField(max_length=2, choices=Chai_Type_Choice)
    date = models.DateField()

    def __str__(self):
        return self.name


class Chai_Review(models.Model):
    chai = models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name='Reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField( max_length=500)
    date_added = models.DateTimeField()
    def __str__(self):
     return f' {self.user.name} review for {self.chai.name}'

class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    chai_varietes = models.ManyToManyField(ChaiVariety,related_name='Stores')
    def __str__(self):
        return self.name
    


class Chai_Certificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issued_date = models.DateTimeField()
    valid_until = models.DateTimeField()

    def __str__(self):
        return f' Certificate for  {self.name.chai}'


