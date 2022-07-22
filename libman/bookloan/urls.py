from django.urls import path
from .views import BookLoanList,ReturnBook,LoanBookDetail
urlpatterns = [
	path('<int:pk>',BookLoanList.as_view(),name='book-loan-list'),
	path('return-book/<int:pk>',ReturnBook.as_view(),name='return-book'),
	path('loan-book-detail/<int:pk>',LoanBookDetail.as_view(),name='loan-book-detail'),
]
