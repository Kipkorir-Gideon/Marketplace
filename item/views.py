from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm
from .models import Item

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
    }

    return render(request, 'items/new_item.html', context)