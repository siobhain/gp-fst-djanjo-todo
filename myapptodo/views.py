from django.shortcuts import render
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()  # returns query set & content is dictionary with all items
    context = {
        'items': items
    }
    return render(request, 'myapptodo/todo_template.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_description')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')
    return render(request, 'myapptodo/add_template.html')
