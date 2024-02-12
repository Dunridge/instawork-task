from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    members = [
        # TODO: fix the issue so that you have at least one user (OPTIONAL - if you have time)
        # {
        #     'id': 1, # start with 1 because 0 evaluates to false  
        #     'name': 'Adrien Olczak', 
        #     'position': 'admin', 
        #     'phone': '415-310-1619',
        #     'email': 'adrien@instaworks.com'
        # }
    ]
    
    if 'members' not in request.session:
        request.session['members'] = members

    # request.session.clear() # Use this to clear the session
    
    # TODO: pass the initial array with members to the session 

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


        members = request.session.get('members', [])
        new_member_id = len(members) + 1
        new_member = {
            'id': new_member_id, # TODO: fix this bug 
            'name': name,
            'position': position,
            'phone': phone,
            'email': email,
        }
        print('member [new member]', new_member)
        print('members [add]:', len(members))

        members.append(new_member)
        request.session['members'] = members
        print('members [new member]', members)
        
        return redirect('index')
    
    # TODO: extract the add_member content into a component and then call it in each of the forms
    return render(request, 'add_member/index.html', context)

def edit(request, member_index=None): 
    members = request.session.get('members', [])

    print('members', members)
    print('member_index [edit]',member_index)
    print('len(members)', len(members))
    
    if 0 <= member_index <= len(members): 
        arr_index = member_index - 1
        member_to_edit = members[arr_index]

        context = {
            'is_add_form': False,
            'member_to_edit': member_to_edit
        }

        if request.method == 'POST': 
            return HttpResponse('EDIT REQUEST POST REACHED')

        return render(request, 'edit_member/index.html', context)
    else: 
        return HttpResponse('Invalid member index')
        
def delete(request, member_id): 
    # TODO: fix the bug with index, probably instead of giving id as numbers give unique ids from the uuid library
    if request.method == 'DELETE':
        members = request.session.get('members', [])
        member_index = next((index for index, member in enumerate(members) if member['id'] == member_id), None)
        
        if member_index is not None:
            deleted_member = members.pop(member_index)
            request.session['members'] = members
            return HttpResponse(f"Delete member with id {member_id}")
        else: 
            return HttpResponse(f"Error deleting member with id {member_id}")
            
    
# TODO: probably will have to add an update route as well 