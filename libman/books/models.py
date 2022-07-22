from django.db import models

from students.models import Student

# Create your models here.
class Book(models.Model):
		title = models.CharField(max_length=200)
		author = models.CharField(max_length=200,blank=True,null=True)
		description = models.TextField(blank=True, null=True)
		category = models.TextField(blank=True, null=True)
		quantity = models.BigIntegerField(blank=True,null=True)
		is_available = models.BooleanField(blank=True,null=True)
		def __str__(self):
			return self.title
		# override the save method
		def save(self,*args,**kwargs):
			if self.quantity > 0:
				self.is_available= True
			else:
				self.is_available=False
			super(Book,self).save(*args,**kwargs)