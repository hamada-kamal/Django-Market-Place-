from django import forms
from . models import Profile
from products.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _



class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=25,)
    last_name = forms.CharField(max_length=25)
    phone = forms.CharField(max_length=11)
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username',_('first_name'),_('last_name'),_('email'), _('phone'),'password1', 'password2',]


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email','first_name','last_name']



class ProfileForm(forms.ModelForm):
    # image = forms.ImageField(label='Profile Image',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image','address']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone',]
