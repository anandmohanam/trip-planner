"""samsung URL Configurationmyapp/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from myapp.views import *
from myapp.models import Package
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('packages/', packages, name='packages'),
    path('package_detail/<int:pk>', package_details, name='package_details'),
    path('payment/', payment, name='payment'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls, name='admin_login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
