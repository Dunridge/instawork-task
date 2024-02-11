from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    members = [
        { 
            'name': 'Adrien Olczak', 
            'position': 'admin', 
            'phone': '415-310-1619',
            'email': 'adrien@instaworks.com'
        },
        { 
            'name': 'Adrien Olczak', 
            'position': 'admin', 
            'phone': '415-310-1619',
            'email': 'adrien@instaworks.com'
        },
        { 
            'name': 'Adrien Olczak', 
            'position': 'admin', 
            'phone': '415-310-1619',
            'email': 'adrien@instaworks.com'
        },
        { 
            'name': 'Adrien Olczak', 
            'position': 'admin', 
            'phone': '415-310-1619',
            'email': 'adrien@instaworks.com'
        },
        { 
            'name': 'Adrien Olczak', 
            'position': 'admin', 
            'phone': '415-310-1619',
            'email': 'adrien@instaworks.com'
        }
    ]

    context = {
        'members': members,
    }

    return render(request, 'instawork_app/index.html', context)

def add(request): 
    context = {}
    return render(request, 'add_member/index.html', context)

def edit(request): 
    context = {}
    return render(request, 'edit_member/index.html', context)