"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from mysite import settings

#from django.contrib.auth import views as auth_views

from main import views as main_view
from manager import views as manager_view
from account import views as account_view
from successful_send import views as successful_send_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view.index, name='home'),
    path('manager/', manager_view.index, name='manager'),
    path('manager/form/<str:pk>/', manager_view.update_form, name='manager_form'),
    path('successful-send/', successful_send_view.index, name='successful_send'),
    path(settings.LOGIN_URL, account_view.UserLoginView.as_view(), name='login'),
    path(settings.REGISTER_URL, account_view.UserRegistrationView.as_view(), name='register'),
    path(settings.LOGOUT_URL, account_view.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)