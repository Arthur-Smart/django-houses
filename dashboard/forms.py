from django import forms

from .models import Tenant
from core.models import Properties

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('category', 'name', 'user_image', 'room_No', 'phone', 'cost', 'move_in_date', 'clearance')
        widgets = {
            'category':forms.Select( attrs={
                'class':'create-content-form-input'
            }),
            'name':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Tenant name'
            }),
            'room_No':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Room No'
            }),
            'user_image':forms.FileInput( attrs={
                'class':'create-content-form-input',
            }),
            'phone':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Tenant Contacts'
            }),
            'move_in_date':forms.DateInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Eg; 12-03-2023'
            }),
            'cost':forms.NumberInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Cost'
            }),
            'clearance':forms.CheckboxInput( attrs={
                'class':'create-content-form-input',
            }),
        }

class CreatePropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ('title', 'location', 'image', 'bedrooms', 'cost', 'description', 'availability')
        widgets = {
            'title':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Tenant name'
            }),
            'location':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Room No'
            }),
            'image':forms.FileInput( attrs={
                'class':'create-content-form-input',
            }),
            'cost':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Tenant Contacts'
            }),
            'move_in_date':forms.DateInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Eg; 12-03-2023'
            }),
            'bedrooms':forms.NumberInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Cost'
            }),
            'description':forms.Textarea( attrs={
                'class':'create-content-form-input',
            }),
            'availability':forms.CheckboxInput( attrs={
                'class':'create-content-form-input',
            }),
        }        