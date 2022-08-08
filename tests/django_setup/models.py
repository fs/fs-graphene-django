from django.db import models


class Author(models.Model):
    """Test author model."""

    name = models.CharField(max_length=255)


class Post(models.Model):
    """Test post model."""

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
