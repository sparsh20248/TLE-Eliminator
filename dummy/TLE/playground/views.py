from django.shortcuts import render

def start_app(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')