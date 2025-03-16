def services(request):
    return {
        'service_title': 'Services',
        'service_description': 'Lorem ipsum dolor sit amet consectetur.',
    }

def portfolio(request):
    return {
        'portfolio_title': 'Portfolio',
        'portfolio_description': 'Lorem ipsum dolor sit amet consectetur.',
    }

def history(request):
    return {
        'history_title': 'About',
        'history_description': 'Lorem ipsum dolor sit amet consectetur.',
    }

def staff(request):
    return {
        'staff_title': 'Our Amazing Team',
        'staff_description': 'Lorem ipsum dolor sit amet consectetur.',
        'staff_bottom_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut eaque, laboriosam veritatis, quos non quis ad perspiciatis, totam corporis ea, alias ut unde.',
    }

def contacts(request):
    return {
        'contact_title': 'Contact Us',
        'contact_description': 'Lorem ipsum dolor sit amet consectetur.',
    }