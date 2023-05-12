from django import forms

from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('category', 'title', 'location', 'image', 'description', 'bedrooms', 'cost', 'availability',)
        widgets = {
            'category':forms.Select( attrs={
                'class':'create-content-form-input'
            }),
            'title':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Enter Title'
            }),
            'location':forms.TextInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Enter Location'
            }),
            'image':forms.FileInput( attrs={
                'class':'create-content-form-input',
            }),
            'description':forms.Textarea( attrs={
                'class':'create-content-form-input',
                'placeholder':'Type Description'
            }),
            'bedrooms':forms.NumberInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Number of bedrooms'
            }),
            'cost':forms.NumberInput( attrs={
                'class':'create-content-form-input',
                'placeholder':'Rent per month'
            }),
            'availability':forms.CheckboxInput( attrs={
                'class':'create-content-form-input',
            }),
        }