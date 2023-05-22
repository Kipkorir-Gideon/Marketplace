from django.shortcuts import render, get_object_or_404

from .models import Item

def item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=item_id)[0:3]

    context = {
        'item': item,
        'related_items': related_items
    }

    return render(request, 'items/item.html', context)