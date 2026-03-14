from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/',default='profiles/default.png')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.username} Profile'