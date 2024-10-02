from django.db import models
from django.utils import timezone




class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class TodoTask(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,default='general_category',on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title



