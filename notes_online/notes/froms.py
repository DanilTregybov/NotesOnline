from .models import Theme, Note
from django.forms import ModelForm, TextInput, Textarea


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ["theme_name"]
        widgets = {
            "theme_name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Enter theme name'
            }),
        }

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'name', 'text']
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note name"
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
        }
