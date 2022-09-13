from django.urls import path 
from.views import UserCreate,BookListCreateView,BookRetrievUpdateDestroyView,Bookslist



urlpatterns = [
    path("api/",Bookslist.as_view(),name="book_list"),
    path("bookcreate/",BookListCreateView.as_view(),name="List_create_view"), 
    path('book/<int:pk>/',BookRetrievUpdateDestroyView.as_view(),name="update_delete_view"),
    path('registration/',UserCreate.as_view(),name="registration"),
   
]
