from django.shortcuts import render

def index(request):
    return render(request, 'instawork_app/index.html')