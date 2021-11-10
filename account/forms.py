from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"exampleInputEmail1" ,"aria-describedby":"emailHelp","placeholder":"Enter email"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control" ,"id":"exampleInputPassword1" ,"placeholder":"Password"}))

class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username','first_name','email')

    widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','required':"required",'placeholder':"Username"}),         
            'first_name':forms.TextInput(attrs={'class':'form-control','required':"required",'placeholder':"Username"}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),       
    }

    labels={
        'username':'Username',
        'first_name':'Firstname',
        'email':'Email',
        'password':'Password',
        'password2':'Password Again'
    }

    # You can provide a clean_<fieldname>() method to any of your form fields in order to clean the value 
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
                'first_name':forms.TextInput(attrs={'class':'form-control','required':"required",'placeholder':"First name"}),         
                'last_name':forms.TextInput(attrs={'class':'form-control','required':"required",'placeholder':"Last name"}),
                'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Email"}),
                    
        }

        labels={
            'first_name':'first_name',
            'first_name':'Firstname',
            'email':'Email',
            
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
    
        widgets = {
                'date_of_birth':forms.DateTimeInput(attrs={'class':'form-control','required':"required",'placeholder':"mm/dd/yyyy"}),         
                'photo':forms.ClearableFileInput(attrs={ 'class':"custom-file-input form-control" ,'id':"customFile"})
        }
        

        labels={
            'date_of_birth':'Username',
            'photo':'Choose file',
            
        }