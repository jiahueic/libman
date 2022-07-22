from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class BookList(LoginRequiredMixin,ListView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = Book
	template_name='books/book_list.html'
	context_object_name ='books'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		search_input = self.request.GET.get('search-area')
		if search_input:
			context['books'] = context['books'].filter(title__icontains=search_input)
		return context

class BookCreate(CreateView):
	model = Book
	fields=["title","description","author","category","quantity"]
	template_name = 'books/book_create.html'
	success_url= reverse_lazy('book-list')
class BookUpdate(UpdateView):
	model = Book
	fields=["title","description","author","category","quantity"]
	template_name = 'books/book_create.html'
	success_url= reverse_lazy('book-list')
class BookDelete(DeleteView):
	model = Book
	success_url=reverse_lazy('book-list')
	context_object_name = 'book'
	template_name = 'books/book_delete.html'
class BookDetail(DetailView):
	model = Book
	context_object_name = 'book'
	template_name = 'books/book_detail.html'