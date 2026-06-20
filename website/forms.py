from django import forms
from .models import Comment
from blog.models import Post


class ContactForm(forms.Form):
    fullName = forms.CharField(label="full name", max_length=100)
    email = forms.EmailField(label="email")
    subject = forms.CharField(label="subject", max_length=200)
    message = forms.CharField(
        label="message",
        widget=forms.Textarea(attrs={"placeholder": "Enter your request"}),
    )



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
