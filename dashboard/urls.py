from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard_View, name='dashboard'),
    path('dashboard/create-tenant/', views.create_tenant, name='create_tenant'),
    path('dashboard/edit-tenant/<int:pk>/', views.edit_tenant, name='edit_tenant'),
    path('dashboard/delete-tenant/<int:pk>/', views.delete_tenant, name='delete_tenant'),
    path('tenant/<slug:slug>', views.tenant_View, name='tenant'),
    path('dashboard/create/', views.create_Content, name='create-house'),
    path('dashboard/create-property/', views.create_property, name='create-property'),
    path('dashboard/edit-property/<int:pk>', views.edit_property, name='edit_property'),
    path('dashboard/delete-property/<int:pk>', views.delete_property, name='delete_property'),
    path('dashboard/edit/<int:pk>/', views.edit_house, name='edit-house'),
    path('dashboard/delete/<int:pk>/', views.delete_house, name='delete-house'),
    path('dashboard/owner-property/', views.created_property, name='created_property'),
    # path('create-property/', views.create_Content_Property, name='create')
]