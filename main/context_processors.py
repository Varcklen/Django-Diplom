def services(request):
    return {
        'service_title': 'Services',
        'service_description': 'We provide a wide range of services',
    }

def portfolio(request):
    return {
        'portfolio_title': 'Portfolio',
        'portfolio_description': 'We have long-term experience in this area',
    }

def history(request):
    return {
        'history_title': 'About',
        'history_description': 'Our history is quite extensive',
        'history_inspire': 'Be Part <br/> Of Our <br/> Story!',
    }

def staff(request):
    return {
        'staff_title': 'Our Amazing Team',
        'staff_description': 'Our professionals work tirelessly',
        'staff_bottom_description': 'You can use the services of our employees or become part of our company',
    }

def contacts(request):
    return {
        'contact_title': 'Contact Us',
        'contact_description': 'Write to us about your problem and we will help you solve it',
        'contact_send_message': 'Send Message',
        'contact_name_require': 'A name is required.',
        'contact_email_require': 'An email is required.',
        'contact_email_invalid': 'Email is not valid.',
        'contact_phone_require': 'A phone number is required.',
        'contact_message_require': 'A message is required.',
    }

def portfolio_modals(request):
    return {
        'portfolio_modals_close_project': 'Close Project',
    }