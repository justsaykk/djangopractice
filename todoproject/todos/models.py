from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    # level = models.IntegerField(default=1)
class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
