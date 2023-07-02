from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()  # returns query set & content is dictionary with all items
    context = {
        'items': items
    }
    return render(request, 'myapptodo/todo_template.html', context)

# This was how my own tiny form was handled before forms.py imported
# def add_item(request):
#     if request.method == 'POST':
#         name = request.POST.get('item_description')
#         done = 'done' in request.POST
#         Item.objects.create(name=name, done=done)
#         return redirect('get_todo_list')
#     return render(request, 'myapptodo/add_template.html')


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
        return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'myapptodo/add_template.html', context)
