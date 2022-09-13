from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from  Bookapi.models import Book
from django.shortcuts import redirect, render,HttpResponse

def home(request):
    return render(request,"homee.html")
def all_books (request):
    emps =Book.objects.all()
    context = {
        'empss':emps
    }
    print(context)
  
    return render(request,"home.html",context)
   
  
def add_book(request):
    if request.method=="POST":
        title = request.POST['title']
        author = request.POST['author']
        Genre =  request.POST['Genre']
        Favorite = request.POST['Favorite']
        Review = int( request.POST['Review'])
      
        new_book = Book(title=title,author=author,Genre=Genre,Favorite=Favorite,Review=Review)
        new_book.save()
        return HttpResponse('Book added successfuly')
    elif request.method=="GET":
        return render(request,'add_book.html')    
    else:
        return HttpResponse("An exception occured emplyee cannot be added")
def remove_book(request,book_id=0):
    if book_id:
        try:
            emp_tobe_removed = Book.objects.get(id=book_id)
            emp_tobe_removed.delete()
            return HttpResponse("Book Removed successfully")
        except:
            return HttpResponse("PLEASE ENTER A VALID Book ID")
    emps = Book.objects.all()
    context = {
        'emps':emps
    }
    return render(request,"remove_book.html",context)   
def update_book(request,book_id):
    booked = Book.objects.get(id=book_id)
  
    # employeed.save()
    # return HttpResponse('employee edited successfuly')
    emps = Book.objects.all()
    context = {
        'empss':emps, 
        'booked':booked
        
    }
    return render(request,"update_book.html",context)
def edit_book(request,book_id):
    item = Book.objects.get(id=book_id)
    item.title = request.POST['title']
    item.Favorite = request.POST['Favorite']
    item.save()
    return redirect('books')
def user_profile(request):
    emps = User.objects.all()
    context ={
        'empss':emps 
        
    }
    print(context)
    return render(request,"userprofile.html",context)
    
    
        
      

# Create your views here.
