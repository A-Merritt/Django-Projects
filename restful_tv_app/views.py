from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows/new')

def addshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows')
    
    
    elif (request.method =="POST"):
        Show.objects.create(
            title = request.POST["title"],
            network = request.POST["network"],
            date = request.POST["date"],
            description = request.POST["description"]
        )
        return redirect('/shows/new')
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'new.html', context)

def specificshow(request, Show_id):
    context = {
        'shows': Show.objects.all(),
        'show': Show.objects.get(id=Show_id)
    }
    return render(request, 'show.html', context)

def edit(request, Show_id):
    one_show = Show.objects.get(id=Show_id)
    context = {
        'show': one_show
    }
    return render(request, 'update.html', context)

def destroy(request):
    pass

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'allShows.html', context)

def destroy(request, Show_id):
    to_delete = Show.objects.get(id=Show_id)
    to_delete.delete()
    return redirect('/shows')

def update(request, Show_id):
    to_update = Show.objects.get(id=Show_id)
    to_update.title = request.POST['title']
    to_update.network = request.POST['network']
    to_update.date = request.POST['date']
    to_update.description = request.POST['description']

    return redirect('/shows')
