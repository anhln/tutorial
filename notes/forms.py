from cProfile import label
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs= { 'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'text': 'Write the content of note here'
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('Title must have a Django')
        else: 
            return title 
          