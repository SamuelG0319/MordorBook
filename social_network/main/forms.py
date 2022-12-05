from django import forms
<<<<<<< HEAD
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    message = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
=======

from . models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
>>>>>>> main
