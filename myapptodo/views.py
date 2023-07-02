from django.shortcuts import render
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'myapptodo/todo_template.html', context)


def add_item(request):
    return render(request, 'myapptodo/add_template.html')
