from django.shortcuts import render

def item(request):
    return render(request, 'items/item.html')