from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    mobile=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username

class Newconnection(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE, null=True)
    gen=models.CharField(max_length=100,null=True)
    nationality=models.CharField(max_length=100,null=True)
    merriedstatus=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    related=models.CharField(max_length=100,null=True)
    fname=models.CharField(max_length=100,null=True)
    lname=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    connection=models.CharField(max_length=100,null=True)
    registration=models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    zipcode=models.CharField(max_length=100,null=True)
    img=models.FileField(null=True)
    cost=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.user.username


class Addstaff(models.Model):
    staffid=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Bookcylinder(models.Model):
    user=models.ForeignKey(Newconnection,on_delete=models.CASCADE, null=True)
    gassize=models.CharField(max_length=100,null=True)
    booknumber=models.CharField(max_length=100,null=True)
    bookdate=models.CharField(max_length=100,null=True)
    bookstatus=models.CharField(max_length=100,null=True)
    reffercost=models.CharField(max_length=100,null=True)
    assignto=models.CharField(max_length=100,null=True)
    responsetime=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.user.user.username+" "+(self.booknumber)
