from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from house.models import Category
# Create your models here.
class Tenant(models.Model):
    user = models.ForeignKey(User, related_name='tenants', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='tenants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # user_image = models.ImageField(upload_to="post_images", default='default.jpg')
    user_image = CloudinaryField('image')
    room_No = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    phone = models.CharField(max_length=10)
    cost = models.IntegerField()
    move_in_date = models.CharField(max_length=100)
    clearance = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

