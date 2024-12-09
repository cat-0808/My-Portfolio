from django.shortcuts import render
from .models import MainPage, Introduction, MainPageImage, PhotoGrid, SocialPlatform

def Home (request):
    entries = MainPage.objects.all()
    introduction = Introduction.objects.all()
    images = MainPageImage.objects.all()
    return render(request, 'home.html', {'MainPage': entries, 'Introduction': introduction, 'MainPageImage': images})

def Projects(request):
    photos = PhotoGrid.objects.all()
    # Split data into three columns
    column1 = photos[::3]  # Every 3rd starting from the first
    column2 = photos[1::3] # Every 3rd starting from the second
    column3 = photos[2::3] # Every 3rd starting from the third

    context = {
        'column1': column1,
        'column2': column2,
        'column3': column3,
    }
    return render(request, 'projects.html', context)

def platforms_view(request):
    platforms = SocialPlatform.objects.all()
    return render(request, 'platforms.html', {'platforms': platforms})
# Create your views here.
