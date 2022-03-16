from django.conf import settings
from django.db import models

# from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    position = models.TextField(blank=True, max_length=30)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.username
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    class Meta:
        ordering = ['-publish_date']

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=155, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title



class Executive(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    contacts = models.TextField(blank=True)

    def __str__(self):
        return self.name