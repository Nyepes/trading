from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from events.models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),label='')
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),label='')
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),label='')

    class Meta:
        model = User
        fields  = ('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     if commit:
    #        user.save()
    #     return User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('initial_equity',)