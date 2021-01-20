from django.db import models
from authapp.models import User


class Chat(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="first_user_id")
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="second_user_id")


class Message(models.Model):
    text = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
