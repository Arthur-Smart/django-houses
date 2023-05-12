from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  django.utils.text import slugify

from .models import Tenant
from house.forms import HouseForm
from .forms import TenantForm, CreatePropertyForm

from core.models import Userprofile, Properties
from house.models import House, Category, Booked_house
# Create your views here.
@login_required(login_url='login')
def dashboard_View(request):
    user_profile = Userprofile.objects.get(user = request.user)
    return render(request, 'dashboard/dashboard.html', {'user_profile':user_profile})

#create house
@login_required(login_url='login')
def create_Content(request):
    user_profile = Userprofile.objects.get(user = request.user)
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid:
            title = request.POST.get('title')
            house = form.save(commit=False)
            house.user = request.user
            house.owner_pic = user_profile.image
            house.owner_name = user_profile.user
            house.slug = user_profile.slug
            house.save()
            messages.success(request, 'House created Successfully')

            return redirect('dashboard')
    else:
        form = HouseForm()
        context ={'form':form, 'header': 'Create House'}
    return render(request, 'dashboard/create.html', context)

#edit house
@login_required(login_url='login')
def edit_house(request, pk):
    house = House.objects.filter(user=request.user).get(pk=pk)
    if request.method =='POST':
        form = HouseForm(request.POST, request.FILES, instance=house)

        if form.is_valid:
            form.save() 
            messages.success(request, 'House has been edited ')

            return redirect('dashboard')   
    else:
        form = HouseForm(instance=house)
        context ={'form':form, 'header': 'Edit House'}
        return render(request, 'dashboard/create.html', context)

#Delete house    
@login_required(login_url='login')
def delete_house(request, pk):
    house = House.objects.filter(user=request.user).get(pk=pk)
    house.delete()

    return redirect('dashboard')

#Create tenant
@login_required(login_url='login')
def create_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST, request.FILES)
        if form.is_valid:
            name = request.POST.get('name')
            tenant = form.save(commit=False)
            tenant.user = request.user
            tenant.slug = slugify(name)

            tenant.save()
            return redirect('dashboard')
    else:
         form = TenantForm()
         context={'form': form}
    
    return render(request, 'dashboard/create_tenant.html', context)    

#Edit tenant
@login_required(login_url='login')
def edit_tenant(request, pk):
    tenant = Tenant.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)

        if form.is_valid:
            form.save()
            return redirect('dashboard')
    else:
        form = TenantForm(instance=tenant)
        context ={'form':form}
    return render(request, 'dashboard/create_tenant.html', context)

@login_required(login_url='login')
def delete_tenant(request,pk):
    tenant = Tenant.objects.filter(user=request.user).get(pk=pk)
    tenant.delete()
    return redirect('dashboard')

def created_property(request):
    return render(request, 'dashboard/created_properties.html')

@login_required(login_url='login')
def create_property(request):
    user_profile = Userprofile.objects.get(user = request.user)
    if request.method == 'POST':
        form = CreatePropertyForm(request.POST, request.FILES)
        title = request.POST.get('title')
        property_object = form.save(commit=False)
        property_object.user = request.user
        property_object.slug = user_profile.slug
        property_object.profileImage = user_profile.image
        property_object.owner_name = user_profile.user

        if form.is_valid():
            property_object.save()
            return redirect('dashboard')
    else:
        form = CreatePropertyForm()    
        return render(request, 'dashboard/create.html', {'form':form, 'header':'Create Property'})
    
#Edit property
def edit_property(request, pk):
     property = Properties.objects.filter(user=request.user).get(pk=pk)
     if request.method == 'POST':
        form = CreatePropertyForm(request.POST, instance=property)

        if form.is_valid:
            form.save()
            return redirect('created_property')
     else:
        form = CreatePropertyForm(instance=property)
        context ={'form':form}
     return render(request, 'dashboard/create.html', context)

#Delete property
def delete_property(request, pk):
    property = Properties.objects.filter(user=request.user).get(pk=pk)
    property.delete()
    return redirect('created_property')

@login_required(login_url='login')
def tenant_View(request, slug):
    tenant = Tenant.objects.get(slug=slug)
    # len_of_tenant = tenant.count()
    # print(len_of_tenant)
    context ={'tenant':tenant}
    return render(request, 'dashboard/tenant.html', context)


def booked_houses(request):
    house = House.objects.all()
    booking = Booked_house.objects.all()
    print(booking)
    return render(request, 'dashboard/dashboard.html', {'booking':booking}) 

@login_required
def chat_View(request, pk):
    return render(request, 'dashboard/messages.html')