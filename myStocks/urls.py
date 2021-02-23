from django.contrib import admin
from django.urls import path, include #added include to include quotes urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stockQuotes.urls')),
]
