from django.db import models
import datetime
from books.models import Book
from students.models import Student
# Create your models here.
class BookLoan(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
	book = models.ForeignKey(Book,on_delete=models.CASCADE,blank=True,null=True,limit_choices_to={'is_available':True})
	borrow_date = models.DateField(blank=True, null=True)
	issued_retured_date = models.DateField(blank=True, null=True)
	return_date = models.DateField(blank=True, null=True)
	

	#override save method to calculate issued_returned_date
	def save(self,*args,**kwargs):
			self.issued_retured_date = self.borrow_date + datetime.timedelta(days=14)
			super(BookLoan,self).save(*args,**kwargs)

