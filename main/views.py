from django.shortcuts import render
from .models import *

# Create your views here.


def index_view(request):

    photos = Photo.objects.all()
    last_photo = Photo.objects.last()
    category = Category.objects.all()

    data = {
        'photos': photos, 
        'last_photo': last_photo,
        'categories': category
        }

    return render(request, 'index.html', context=data)


def photo_detail(request, photo_id):

    photo_detail = Photo.objects.get(id=photo_id)
    data = {"photo_detail": photo_detail}
    
    if not request.session.get('photo_detail'):
        request.session['photo_detail'] = []
        request.session['photo_detail'].append(photo_detail.id)
        photo_detail.views += 1
    elif photo_detail.id not in request.session['photo_detail']:
        photo_detail.views += 1
        request.session['photo_detail'].append(photo_detail.id)
        request.session.save()

    photo_detail.save()


    return render(request, 'photo_detail.html', data)


def category_view(request, category_id):

    categories = Category.objects.get(id=category_id)
    photos = Photo.objects.filter(category=categories)
    data = {'photos': photos, 'categories': categories}

    return render(request, "category.html", data)