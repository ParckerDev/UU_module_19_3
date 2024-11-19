from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=1200)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title