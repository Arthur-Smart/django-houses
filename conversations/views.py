from django.shortcuts import render, get_object_or_404, redirect

from house.models import House

from .models import Conversation, ConversationMessage
from .forms import ConvesationForm

def new_conversation(request, house_pk):
    house = get_object_or_404(House, pk=house_pk)

    if house.user == request.user:
        return redirect('dashboard')

    conversations = Conversation.objects.filter(house=house).filter(members__in=[request.user.id])
    
    if conversations:
        pass

    if request.method == 'POST':
        form = ConvesationForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(house=house)
            conversation.members.add(request.user)
            conversation.members.add(house.user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            print(conversation_message)
            return redirect('dashboard')
        
    else:
        form = ConvesationForm()

    return render(request, 'dashboard/messages.html', {'form':form})


def inbox_conversations(request):
    conversations = ConversationMessage.objects.all()
    print( conversations)
    return render(request, 'dashboard/dashboard.html', {'conversations':conversations})  
    