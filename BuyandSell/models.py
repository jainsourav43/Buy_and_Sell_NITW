from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
	name = models.CharField(max_length=100,default="ram")
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	email= models.EmailField()
	contactno=models.CharField(max_length=10)
	image=models.FileField(default='jon.png')
	
	# def __str__(self):
	# 	return self.item_name


class item(models.Model):
	item_name=models.CharField(max_length=100)
	item_id=models.CharField(max_length=50)
	price  = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	description =models.CharField(max_length=100)
	image=models.FileField()
	available =models.BooleanField(default=False)
	report=models.FileField(null=True)




