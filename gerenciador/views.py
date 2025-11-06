from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, 'gerenciador/about.html')