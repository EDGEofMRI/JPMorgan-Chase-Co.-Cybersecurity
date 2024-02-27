"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django_otp.admin import OTPAdminSite

# Create two instances of the admin site
admin_site_with_totp = OTPAdminSite()
admin_site_without_totp = admin.site  # Use the default admin site without TOTP

urlpatterns = [
    path('admin-with-totp/', admin_site_with_totp.urls),
    path('admin/', admin_site_without_totp.urls),
]

# Set the admin site for each instance
OTPAdminSite.admin_site = admin_site_with_totp
admin.site.admin_site = admin_site_without_totp