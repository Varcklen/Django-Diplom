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
        'history_inspire': 'Be Part <br /> Of Our <br /> Story!',
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
        'contact_send_message': 'Send Message',
        'contact_success': 'Form submission successful!',
        'contact_fail': 'Error sending message!',
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