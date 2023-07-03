from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {'form': form
               }
    return render(request, 'myapptodo/edit_template.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


    
