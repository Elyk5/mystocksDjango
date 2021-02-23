from django.urls import path
from . import views #importing from this quotes directory

urlpatterns = [
	path('', views.home, name="home"),
	path('about.html', views.about, name="about"),
   
]
