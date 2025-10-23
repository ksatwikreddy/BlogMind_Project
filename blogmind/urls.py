# blogmind/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 🌟 Re-add this line to route the root URL to your core app
    path('', include('core.urls')), 
]