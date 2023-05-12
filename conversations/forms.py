from django import forms

from .models import ConversationMessage

class ConvesationForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
       