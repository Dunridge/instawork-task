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

    context = {
        'is_add_form': True
    }

    if request.method == 'POST': 
        name = request.POST.get('name')
        position = request.POST.get('position')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        new_member = {
            'name': name,
            'position': position,
            'phone': phone,
            'email': email,
        }
        members = request.session.get('members', [])
        print('members [add]:', len(members))

        members.append(new_member)
        request.session['members'] = members
    
    # TODO: extract the add_member content into a component and then call it in each of the forms
    return render(request, 'add_member/index.html', context)

def edit(request): 
    
    context = {
        'is_add_form': False
    }

    return render(request, 'edit_member/index.html', context)