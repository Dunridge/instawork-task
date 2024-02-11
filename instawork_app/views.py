from django.shortcuts import render

def index(request):
    members = [
        {'name': 'John Doe', 'position': 'Developer'},
        {'name': 'Jane Doe', 'position': 'Designer'},
        {'name': 'Jane Doe', 'position': 'Designer'},
        {'name': 'Jane Doe', 'position': 'Designer'},
        {'name': 'Jane Doe', 'position': 'Designer'},
    ]

    context = {
        'members': members,
    }

    return render(request, 'instawork_app/index.html', context)