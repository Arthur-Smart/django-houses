from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import  Userprofile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('phone', 'image', 'about')
        widgets = {
            'phone':forms.TextInput( attrs= {
                'class':'settings-input'
            }),
            'image':forms.FileInput( attrs= {
                'class':'settings-input'
            }),
            'about':forms.Textarea( attrs= {
                'class':'settings-textarea'
            })
        }