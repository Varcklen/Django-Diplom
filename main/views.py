from django.shortcuts import render
from .models import Service, Portfolio, History, Staff, Partner, Contact

# Create your views here.
def index(request):
    services = Service.objects.filter(is_visible=True)
    portfolios = Portfolio.objects.filter(is_visible=True)
    histories = History.objects.filter(is_visible=True)
    staff = Staff.objects.filter(is_visible=True)
    partners = Partner.objects.filter(is_visible=True)
    #contacts = Contact.objects.first()

    context = {
        'services': services,
        'portfolios': portfolios,
        'histories': histories,
        'staff': staff,
        'partners': partners,
        #'contacts': contacts,
    }

    return render(request, 'index.html', context=context)