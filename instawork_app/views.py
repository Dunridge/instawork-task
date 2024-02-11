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

    session_members = request.session.get('members', [])
    all_members = members + session_members
    print('session_members [index]', len(session_members))
    print('members [index]', len(members))
    print('all_members [index]', len(all_members))

    context = {
        'members': all_members,
    }

    return render(request, 'instawork_app/index.html', context)

def add(request): 
    context = {}
    # you need to trigger this from the template
    if request.method == 'POST': 
        new_member = {
            'name': 'Max',
            'position': 'Software engineer',
            'phone': '111 111 1111',
            'email': 'max@gmail.com',
        }
        members = request.session.get('members', [])
        print('members [add]:', len(members))

        members.append(new_member)
        request.session['members'] = members
    
    
    return render(request, 'add_member/index.html', context)

def edit(request): 
    context = {}
    return render(request, 'edit_member/index.html', context)