from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from item.models import Item
from .models import Chat

from .forms import ChatMessageForm

@login_required
def new_chat(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if item.created_by == request.user:
        return redirect('dashboard')
    
    chats = Chat.objects.filter(item=item).filter(members__in=[request.user.id])

    if chats:
        return redirect('chat_detail', id=chats.first().id)

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(request.user)
            chat.members.add(item.created_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()
            messages.success(request, 'Message sent Successfully')

            return redirect('item', item_id=item_id)
    else:
        form = ChatMessageForm()

    context = {
        'item': item,
        'form': form,
    }

    return render(request, 'chat/chat.html', context)

@login_required
def inbox(request):
    chats = Chat.objects.filter(members__in=[request.user.id])

    context = {
        'chats': chats,
    }

    return render(request, 'chat/inbox.html', context)

@login_required
def chat_detail(request, id):
    chat = Chat.objects.filter(members__in=[request.user.id]).get(id=id)

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            chat.save()

            return redirect('chat_detail', id=id)
    else:
        form = ChatMessageForm()

    context = {
        'chat': chat,
        'form': form,
    }

    return render(request, 'chat/chat_detail.html', context)