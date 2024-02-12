from django import forms

class MemberForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    role = forms.ChoiceField(
        choices=[('regular', 'Regular - Can\'t delete members'), ('admin', 'Admin - Can delete members')],
        widget=forms.RadioSelect,
        initial='regular'
    )