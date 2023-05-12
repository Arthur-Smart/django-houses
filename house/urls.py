from django.urls import path

from . import views

urlpatterns = [
    path('<slug:house_slug>/<slug:slug>/', views.house_View, name='house'),
    path('like_house/<int:pk>', views.like_house, name='like_house')
]