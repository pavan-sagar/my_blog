from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)
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
    ordering = ['-date_posted'] # The negative sign means in descending order

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

#We use the LoginRequiredMixin and override the below method to make sure only logged in user can create posts
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#The UserPassesTestMixin along with overriding below method makes sure the logged in user can only update his/her own posts    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
   

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

