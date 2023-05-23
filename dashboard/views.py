from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)

    context = {
        'items': items
    }

    return render(request, 'auth/dashboard.html', context)