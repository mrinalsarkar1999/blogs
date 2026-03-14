from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length = 50,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='posts/images/',blank=True,null=True)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    slug = models.SlugField(unique = True)
    
    def __str__(self):
        return self.title
