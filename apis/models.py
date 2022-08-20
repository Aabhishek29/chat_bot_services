from django.db import models


class ChatModel(models.Model):
    query = models.CharField(max_length=200)
    result = models.TextField()

    def __str__(self):
        return self.query

