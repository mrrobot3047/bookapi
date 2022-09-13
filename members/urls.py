from django.urls import path
from.views import UserRegisterView,UserEditView
from django.contrib.auth import views as auth_views 
from . import views
#from.import views

urlpatterns=[
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('edit_profile/',views.UserEditView.as_view(),name='edit_profile'),
 
    
    
  
]