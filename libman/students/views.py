from django.shortcuts import render,redirect
from .models import Student
from books.models import Book
from bookloan.models import BookLoan
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

class StudentList(ListView):
	model = Student
	template_name='students/student_list.html'
	context_object_name = 'students'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		search_input = self.request.GET.get('search-student') or ''
		if search_input:
			context['students'] = context['students'].filter(name__icontains=search_input)
		return context

class CreateBookLoan(CreateView):
		model = BookLoan
		fields = ['student','book','borrow_date']
		template_name = 'bookloan/create_book_loan.html'
		# return to the library book catalogue after the loan is complete
		success_url="/"
		
		def form_valid(self,form):
			instance = form.save(commit=False)
			book = Book.objects.get(id=instance.book.id)
			# get the book id from the form and check if the book is still available, then subtract
			if book.quantity > 0:
				book.quantity -= 1
				book.save()
				instance.save()
				messages.success(self.request,'Book loan creation successful')
			messages.error(self.request,'The book is not available')
			return super(CreateBookLoan,self).form_valid(form)


class CreateStudent(CreateView):
	model = Student
	fields = "__all__"
	template_name = 'students/create_student.html'
	def get_success_url(self):
		return reverse_lazy('student-list')
class DeleteStudent(DeleteView):
	model = Student
	context_object_name = 'student'
	template_name = 'students/delete_student.html'
	def get_success_url(self):
		return reverse_lazy('student-list')
class UpdateStudent(UpdateView):
	model = Student
	fields = "__all__"
	template_name = 'students/create_student.html'
	def get_success_url(self):
		return reverse_lazy('student-list')
