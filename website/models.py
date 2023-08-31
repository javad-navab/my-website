from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255 , blank=True)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('created_at',)
    def __str__(self):
        return self.name
    
class newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email