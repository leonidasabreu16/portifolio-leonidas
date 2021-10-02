from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html', {})

def portifolio_details(request):
    return render(request, 'core/index.html', {})
