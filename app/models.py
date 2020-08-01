from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(null=True)
    duedate=models.DateTimeField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    img = models.TextField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    content=models.TextField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")

class Study(models.Model):
    title=models.CharField(max_length =100)
    content = models.TextField(null=True)
    # author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="study_posts")
    # study_file = models.FileField(null= True, blank =True, upload_to="")

    def __str__(self):
        return self.title