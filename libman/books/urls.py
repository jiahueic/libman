from django.urls import path
from .views import BookList, BookCreate,BookUpdate,BookDelete,BookDetail
from django.contrib.auth.views import LogoutView
urlpatterns=[
	path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
	path('',BookList.as_view(),name='book-list'),
	path('book-create/',BookCreate.as_view(),name="book-create"),
	path('book-update/<int:pk>',BookUpdate.as_view(),name = 'book-update'),
	path('book-delete/<int:pk>',BookDelete.as_view(),name = 'book-delete'),
	path('book-detail/<int:pk>',BookDetail.as_view(),name = 'book-detail'),

]