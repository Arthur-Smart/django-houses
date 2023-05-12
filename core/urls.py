from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, houses_View, properties_View, user_profile, register, view_user_profile ,search, property_page, category_Houses, like_property

urlpatterns = [    
    path('', index, name='index'),
    path('properties/<int:pk>', like_property, name='like'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('houses/', houses_View, name='houses'),   
    path('properties/', properties_View, name='properties'),
    path('settings/',user_profile, name='settings'),
    path('search/', search, name='search'),
    path('property/<slug:slug>/', property_page, name='property_page'),    
    path('categories/<slug:slug>/', category_Houses, name='house_category'),
    path('profile/<slug:slug>/', view_user_profile, name='user_profile')
    
]