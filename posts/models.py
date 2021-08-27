from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('creation_date','author',)

    def __str__(self):
        return self.author
   

