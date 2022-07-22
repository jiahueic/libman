from django.db import models
# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=250)
	DEGREE_CHOICES=[('Health Sciences','Health Sciences'),('Engineering and IT','Engineering and IT'),('Commerce','Commerce'),("Design","Design")]
	EDUCATION_LEVEL = [('Undergraduate','Undergraduate'),('Postgraduate','Postgraduate')]
	education_level = models.CharField(max_length=100,blank=True,null=True,choices=EDUCATION_LEVEL)
	degree = models.CharField(max_length=300,blank = True, null=True, choices=DEGREE_CHOICES)
	def __str__(self):
		return self.name
