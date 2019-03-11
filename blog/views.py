from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Post




context={'posts':Post.objects.all(),'title': "Pavan's"}

def home(request):
    
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #default required path is <app name>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

