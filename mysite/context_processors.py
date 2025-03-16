from main.models import Contact

def header(request):
    return {
        'header_welcome': 'Welcome To Our Studio!',
        'header_greetings': "It's Nice To Meet You",
        'header_more': 'Tell Me More',
    }

def footer(request):
    contacts = Contact.objects.first()
    
    return {
        'footer_contacts': contacts,
        'footer_copyright': 'Copyright &copy; Your Website 2023',
        'footer_privacy_policy': 'Privacy Policy',
        'footer_terms_of_use': 'Terms of Use',
    }

def navigation(request):
    return {
        'navigation_menu': 'Menu',
    }