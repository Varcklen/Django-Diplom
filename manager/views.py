from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models import UserMessage
from main.forms import UserMessageForm
from django.contrib import messages

def is_manager(user):
    return user.groups.filter(name='manager').exists()

# Create your views here.
@login_required(login_url='login')
@user_passes_test(is_manager)
def index(request):
    messages = UserMessage.objects.filter()

    context = {
        'messages': messages,
    }

    return render(request, 'manager_index.html', context=context)

@login_required(login_url='login')
@user_passes_test(is_manager)
def update_form(request, pk):
    old_message_data = UserMessage.objects.get(id=pk)
    user_message = UserMessageForm(request.POST or None, instance=old_message_data)
    if request.method == 'POST':
        if user_message.is_valid():
            user_message.save()
            return redirect('manager')
        else:
            messages.error(request, 'Your message is not valid.')
            return redirect('manager_form', pk)

    context = {
        'user_message': user_message
    }

    return render(request, 'message_form.html', context=context)