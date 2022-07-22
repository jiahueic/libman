from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from .models import BookLoan
from books.models import Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  DeleteView
import datetime
from django.contrib import messages
# Create your views here.


class BookLoanList(ListView):
	model = BookLoan
	template_name = 'bookloan/book_loan_list.html'
	context_object_name = 'loanbooks'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		# the keyword argument is obtained from studentlist.html
		# when the student id is called 
		context['loanbooks'] = context['loanbooks'].filter(student=self.kwargs['pk'])
		# initialise the amount owed
		context['amountowed'] = 0
		for book in context['loanbooks'] :
			if datetime.date.today() > book.issued_retured_date:
				diff = datetime.date.today() - book.issued_retured_date
				amount = 0.1 * diff.days
				context['amountowed'] = context['amountowed'] + amount
		return context

class ReturnBook(DeleteView):
	model = BookLoan
	template_name = 'bookloan/return_book.html'
	context_object_name = 'loan_book'
	success_url = reverse_lazy('student-list')
	def post(self, request, *args, **kwargs):
		self.object=self.get_object() # add this to load the object
		if self.object is not None:
			book = Book.objects.get(id=self.object.book.id)
			book.quantity += 1
			book.save()
			messages.success(request,'Return is successful')
		messages.error(request,'Return failed')
		return super(ReturnBook,self).post(request,*args, **kwargs)

class LoanBookDetail(DetailView):
	model = BookLoan
	context_object_name = 'loan_book'
	template_name = 'bookloan/loan_details.html'


