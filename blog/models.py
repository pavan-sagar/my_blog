from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#A class based view needs a url in string to redirect to. We used the below to redirect after deleting a post
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})