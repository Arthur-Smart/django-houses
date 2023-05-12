from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import House, Likes



def house_View(request, house_slug, slug):
    house = get_object_or_404(House, slug=slug)
    context ={
        "house":house
    }
    return render(request, 'house/house.html', context)

@login_required(login_url='login')
def like_house(request, pk):
    liked_by = request.user
    house_id  = pk
    print( house_id )
    house = House.objects.get(id= house_id )

    check_like = Likes.objects.filter(  house_id =  house_id , liked_by=liked_by).first()

    if check_like == None:
        new_Like = Likes.objects.create(  house_id = house_id , liked_by=liked_by)
        new_Like.save()
        house.likes = house.likes+1
        house.save()
        return redirect('houses')
    else:
        check_like.delete()
        house.likes = house.likes-1
        house.save()
        return redirect('houses')
