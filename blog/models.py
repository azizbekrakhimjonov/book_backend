from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title


git remote add origin https://github.com/azizbekrakhimjonov/book_backend.git
git branch -M main
git push -u origin main