from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from  django.utils.text import slugify

from .forms import SignUpForm, UserProfileForm
from house.models import House, Category
from .models import Properties, Like, Userprofile

import random

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)

            #Create a user profile
            user_model = User.objects.get(username=username)
            new_user_profile = Userprofile.objects.create(user=user_model, owner_id=user_model.id)
            new_user_profile.save()
            return redirect('settings')
    else:
        form = SignUpForm()
        return render(request, 'core/register.html', {'form':form})


def index(request):
    properties = Properties.objects.all().order_by('?')
    random_properties = properties[:4]
    context ={
        'properties':properties,
        'random_properties':random_properties
    }
    return render(request, 'core/index.html', context)

#Search for a house
def search(request):
    location = request.GET.get('location', '')
    category = request.GET.get('category', '')

    if not  location and category:
        return redirect('index')
    else:
        houses = House.objects.filter(location__icontains=location, category__title__icontains=category)
        return render(request, 'core/search.html', {'houses':houses})

#Create user profile
def user_profile(request):
    user_profile = Userprofile.objects.get(user=request.user)
    print(user_profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid:
            saved_profile = form.save(commit=False)
            saved_profile.slug = slugify(user_profile)
            saved_profile.save()
            return redirect('index')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'core/settings.html', {'form':form, 'user_profile':user_profile})    

#View user profile
def view_user_profile(request, slug):
    profile = get_object_or_404(Userprofile, slug=slug)
    print(profile)
    return render(request, 'core/user_page.html', {'profile': profile})

#Houses view
def houses_View(request):
    min_cost = request.GET.get('min_cost')
    max_cost = request.GET.get('max_cost')
    clear_filters = request.GET.get('clear_filters')
    

    houses = House.objects.all()
    state = False

    #Associated profile
    
    if min_cost and max_cost:
        houses = houses.filter(cost__range=(min_cost, max_cost))
        state = True

    return render(request, 'core/houses.html', {'houses':houses, 'state':state})

#Houses category
def category_Houses(request, slug):
    category = get_object_or_404(Category, slug=slug)
    houses = House.objects.filter(category=category)
    num_houses = len(houses)

    context ={
        'houses':houses,
        'category':category,
        'num_houses':num_houses
    }
          
    return render(request, 'core/category-page.html', context)



#Properties view
def properties_View(request):
    min_cost = request.GET.get('min_cost')
    max_cost = request.GET.get('max_cost')
    clear_filters = request.GET.get('clear_filters')


    properties = Properties.objects.all()
    state = False

    for single_property in properties:
        #likes = single_property.num_of_likes
        print('Yooh')

    if min_cost and max_cost:
        properties = properties.filter(cost__range=(min_cost, max_cost))
        state = True

    if clear_filters:
        properties = Properties.objects.all()
        state = False

    context = {
        'properties':properties,
        'state':state
    }
    return render(request, 'core/properties.html', context)

@login_required(login_url='login')
def like_property(request, pk):
    liked_by = request.user
    property_id = pk
    print(property_id)
    property = Properties.objects.get(id=property_id)

    check_like = Like.objects.filter( property_id= property_id, liked_by=liked_by).first()

    if check_like == None:
        new_Like = Like.objects.create( property_id=property_id, liked_by=liked_by)
        new_Like.save()
        property.num_of_like = property.num_of_like+1
        property.save()
        return redirect('properties')
    else:
        check_like.delete()
        property.num_of_like = property.num_of_like-1
        property.save()
        return redirect('properties')

def property_page(request, slug):
    property = get_object_or_404(Properties, slug=slug)
    return render(request, 'core/property_detail.html', {'property':property})

def user_Account(request):
    return render(request, 'core/settings.html')