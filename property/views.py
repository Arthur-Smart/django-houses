from django.shortcuts import render

# Create your views here.
def property_View(request):
    return render(request, 'property/property.html')
