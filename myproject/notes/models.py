from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    visibility_choices = [
    ('private', 'Private'),
    ('public', 'Public')
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    visibility = models.CharField(max_length=10,
                                  choices=visibility_choices,
                                  default='private'
                                  )
    image = models.ImageField(upload_to="note/images",blank=True,null=True)
    
    def __str__(self):
        return  ("Title: " + self.title + 
                "| Content: " + self.content[:50] +
                "|created at" + str(self.created_at) +
                "|user" + str(self.user) + 
                "|visibility" + self.visibility)
    

# Create your models here.


