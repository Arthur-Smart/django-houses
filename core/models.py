from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    owner_id = models.IntegerField(null=True)
    phone = models.CharField(max_length=50, null=True)
    image = CloudinaryField('image')
    about = models.TextField(null=True)
    slug = models.SlugField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user.username


class Properties(models.Model):
    user = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    # profileImage = models.ImageField(upload_to="post_images", default='default.jpg')
    profileImage = CloudinaryField('image')
    owner_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    location = models.CharField(max_length=40, null=True, blank=True)
    image = CloudinaryField('image')
    bedrooms = models.IntegerField(null=True)
    cost = models.IntegerField()
    description = models.TextField(blank=True)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_of_like = models.IntegerField(default=0)
   

    def __str__(self):
        return self.title
    
class Like(models.Model):
    property_id = models.CharField(max_length=200)
    liked_by = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.liked_by.username    