from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [

{
'author':'Pavan',
'title':'First blogz post',
'date_posted':'06.03.2019',
'content':'This is my post regarding the django blog'
},
{
'author':'Nazim',
'title':'Second blog post',
'date_posted':'07.03.2019',
'content':"I'm planning to go for my higher studies" 
}
]

context={'posts':Post.objects.all(),'title': "Pavan's"}

def home(request):
    
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')