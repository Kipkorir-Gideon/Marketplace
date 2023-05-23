from django.shortcuts import render, redirect
from django.contrib import messages, auth

from item.models import Item, Category

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories,
    }
    
    return render(request, 'core/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/signup.html', context)

def logout(request): 
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out Successfully')
        next_url = request.POST.get('next')
        if next_url and next_url.startswith('/') and not next_url.startswith('//'):
            return redirect(next_url)
        else:
            return redirect('index')