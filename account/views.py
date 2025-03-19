from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self) -> str:
        return self.request.GET.get('next', '/')


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def user_logout(request):
    logout(request)
    return redirect('home')
