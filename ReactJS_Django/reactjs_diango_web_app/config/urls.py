# project_name/config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your app-specific URL patterns here
    path('', include('apps.polls.urls')),
]
