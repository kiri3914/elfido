from django.shortcuts import render
from .models import Food, BookTable, Table, Response, Event, Category

def home(request):
    return render(request, 'home.html')

def menu_category(request, id):
    foods = Food.objects.filter(category__id=id)
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories
    }
    return render(request, 'menu.html', context)


def menu(request):
    foods = Food.objects.all()
    categories = Category.objects.all()

    context = {
        'foods': foods,
        'categories': categories
    }

    return render(request, 'menu.html', context)


def booktable(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        table = request.POST['table']
        phone = request.POST['phone']
        date = request.POST['date']
        persons = request.POST['persons']
        message = request.POST['message']

        book = BookTable.objects.create(
            name=name,
            email=email,
            table=Table.objects.get(id=table),
            phone=phone,
            date=date,
            persons=persons,
            message=message
            )
        book.save()

    table = Table.objects.all()
    context = {
        'tables': table
    }
    return render(request, 'booktable.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subjects = request.POST['subjects']
        message = request.POST['message']

        response = Response(
            name=name,
            phone=phone,
            email=email,
            subjects=subjects,
            message=message
        )
        response.save()

    return render(request, 'contact.html')

def event(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'event.html', context)
    
