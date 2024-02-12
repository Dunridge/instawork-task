from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import MemberForm

def index(request):
    members = []
    
    if 'members' not in request.session:
        request.session['members'] = members

    # request.session.clear() # Use this to clear the session
    
    # TODO: pass the initial array with members to the session 

    session_members = request.session.get('members', [])
    all_members = members + session_members

    context = {
        'members': all_members,
    }

    return render(request, 'instawork_app/index.html', context)

def add(request):

    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            new_member_id = len(request.session.get('members', [])) + 1
            new_member = {
                'id': new_member_id,
                'name': form.cleaned_data['name'],
                'surname': form.cleaned_data['surname'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'role': form.cleaned_data['role'],
            }

            members = request.session.get('members', [])
            members.append(new_member)
            request.session['members'] = members

            return redirect('index')
    else:
        form = MemberForm()  

    context = {
        'is_add_form': True,
        'form': form
    }

    return render(request, 'add_member/index.html', context)

def edit(request, member_index=None):
    members = request.session.get('members', [])
    member_index = int(member_index)

    if member_index is not None and 0 <= member_index <= len(members):
        arr_index = member_index - 1
        member_to_edit = members[arr_index]

        if request.method == 'POST':
            form = MemberForm(request.POST)

            if form.is_valid():
                member_to_edit['name'] = form.cleaned_data['name']
                member_to_edit['surname'] = form.cleaned_data['surname']
                member_to_edit['phone'] = form.cleaned_data['phone']
                member_to_edit['email'] = form.cleaned_data['email']
                member_to_edit['role'] = form.cleaned_data['role']

                request.session['members'] = members

                return redirect('index')
        else:
            form = MemberForm(initial={
                'name': member_to_edit['name'],
                'surname': member_to_edit['surname'],
                'phone': member_to_edit['phone'],
                'email': member_to_edit['email'],
                'role': member_to_edit.get('role', ['Regular']),
            })

        context = {
            'is_add_form': False,
            'member_to_edit': member_to_edit,
            'form': form,
        }

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