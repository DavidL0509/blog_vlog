from django.db import models
from django.contrib.auth.models import User

class Blog_Vlog_Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'blog_images/', null = True, blank = True)
    video = models.FileField(upload_to = 'blog_videos/', null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
