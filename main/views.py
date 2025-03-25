from django.shortcuts import render, redirect
from .models import Service, Portfolio, History, Staff, Partner
from .forms import UserMessageForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    services = Service.objects.filter(is_visible=True)
    portfolios = Portfolio.objects.filter(is_visible=True)
    histories = History.objects.filter(is_visible=True)
    staff = Staff.objects.filter(is_visible=True)
    partners = Partner.objects.filter(is_visible=True)

    user_message = UserMessageForm(request.POST or None)

    if request.method == 'POST':
        if user_message.is_valid():
            user_message.save()
            messages.success(request, 'Your message has been sent. Please wait for a response.')
        else:
            messages.error(request, 'Your message is not valid.')
        return redirect('{}#contact'.format(reverse('home')))
        
    context = {
        'services': services,
        'portfolios': portfolios,
        'histories': histories,
        'staff': staff,
        'partners': partners,
        'user_message': user_message
    }

    return render(request, 'main_index.html', context=context)