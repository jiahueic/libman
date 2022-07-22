from django.urls import path
from .views import StudentList,CreateBookLoan, CreateStudent, DeleteStudent, UpdateStudent

urlpatterns=[
	path('',StudentList.as_view(),name='student-list'),
	path('create-book-loan/',CreateBookLoan.as_view(),name='create-book-loan'),
	path('create-student/',CreateStudent.as_view(),name='create-student'),
	path('delete-student/<int:pk>',DeleteStudent.as_view(),name='delete-student'),
	path('update-student/<int:pk>',UpdateStudent.as_view(),name='update-student'),

]