from django.shortcuts import render, redirect

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