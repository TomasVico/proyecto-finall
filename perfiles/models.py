from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username


class Chat(models.Model):
    user_1 = models.ForeignKey(User, related_name='chats_user_1', on_delete=models.CASCADE)
    user_2 = models.ForeignKey(User, related_name='chats_user_2', on_delete=models.CASCADE)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
