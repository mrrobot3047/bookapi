from django.db import models 
from django.db import models 

class Book(models.Model):
    options=(
       ('fantasy','Fantasy'),
         ('mystery','Mystery'),
         ('literary','Literary'),
         ('non-fiction','Non-Fiction')
     )
    title = models.CharField(max_length=200,null=False)
    author = models.CharField(max_length=200,null=False)
    Genre = models.CharField(max_length=20,choices=options,default='Fantasy')
    Favorite = models.BooleanField(default = False)
    Review = models.FloatField()
    
    def __str__(self):
         return self.title    



# Create your models here.
