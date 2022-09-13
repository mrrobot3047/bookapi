from django.urls import path 
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('all_books/',views.all_books,name="books"),
    path('add_book',views.add_book,name='add_book'),
    path('remove_book',views.remove_book,name='remove_book'),
    path('remove_book/<int:book_id>',views.remove_book,name='remove_book'),
    path('update_book/<int:book_id>',views.update_book,name='update_book'),
    path('edit_book/<int:book_id>',views.edit_book,name='edit_book'),
    path('user_profile',views.user_profile,name="user_profile")
    

  
    
]