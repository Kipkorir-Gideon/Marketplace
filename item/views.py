from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = items.filter(category_id=category_id)

    context = {
        'items': items,
        'categories': categories,
        'query': query,
        'category_id': int(category_id),
    }

    return render(request, 'items/items.html', context)

def item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=item_id)[0:3]

    context = {
        'item': item,
        'related_items': related_items
    }

    return render(request, 'items/item.html', context)

@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item =form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item', item_id=item.id)
    else: 
        form = NewItemForm()

    context = {
        'form': form,
        'title': 'New Item',
    }

    return render(request, 'items/new_item.html', context)

@login_required
def edit_item(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item', item_id=item.id)
    else: 
        form = EditItemForm(instance=item)

    context = {
        'form': form,
        'title': 'Edit Item',
    }

    return render(request, 'items/new_item.html', context)

@login_required
def delete(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    item.delete()

    return redirect('dashboard')