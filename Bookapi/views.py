from django.shortcuts import render 
from django.shortcuts import render
from rest_framework import generics 
from.models import Book
from rest_framework.decorators import api_view 

from .models import Book 
from.serializer import BookSerializer, UserSerializer 
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from django.contrib.auth.models import User 

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (AllowAny,)
class Bookslist(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    filter_backends = [SearchFilter]    
    search_fields = ['Genre']
    permission_classes = (IsAuthenticatedOrReadOnly,)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()    
    serializer_class = BookSerializer 
    permission_classes = (IsAuthenticatedOrReadOnly,)

class BookRetrievUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = (IsAuthenticatedOrReadOnly,)    


# Create your views here.
