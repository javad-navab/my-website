from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class post(models.Model):
    image = models.ImageField(upload_to='blog/' , default='blog/default.jpg')
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return "{}".format(self.title)
    # def snippets(self):
    #     return self.content[:255] +'....'
    
    def get_absolute_url(self):
        return reverse('blog:single' , kwargs={'pid': self.id})

class comment(models.Model):
    post = models.ForeignKey(post , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    massage = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "{}".format(self.name)