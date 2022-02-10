from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)



class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

