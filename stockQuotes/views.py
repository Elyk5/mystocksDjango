from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {}) #home function passing in browser request

def about(request):
	return render(request, 'about.html', {})