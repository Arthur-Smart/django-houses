from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=40)
    # image = models.ImageField(upload_to="post_images", default='default.jpg')
    image = CloudinaryField('image')
    short_description = models.CharField(max_length=500 ,null=True)
    slug = models.SlugField(max_length=40)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class House(models.Model):
    user = models.ForeignKey(User, related_name='houses', on_delete=models.CASCADE)
    # owner_pic = models.ImageField(upload_to="post_images", default='default.jpg')
    owner_pic = CloudinaryField('image')
    owner_name =models.CharField(max_length=40, null=True)
    category = models.ForeignKey(Category, related_name='houses', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    location = models.CharField(max_length=40, null=True, blank=True)
    image = CloudinaryField('image')
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField(null=True)
    cost = models.IntegerField()
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering =  ('-created_at',)

    def __str__(self):
        return self.title

class Likes(models.Model):
    house_id = models.CharField(max_length=200)
    liked_by = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.liked_by.username   

class Booked_house(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username