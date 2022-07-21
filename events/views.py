from django.shortcuts import render

def home(request):
    render(request, 'templates/home.html', {})
