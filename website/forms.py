from django import forms
from .models import Comment, ArticleSuggestion


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

class suggestionForm(forms.ModelForm):
    
    class Meta:
        model = ArticleSuggestion
        fields = ("title", "content")
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'عنوان موضوع پیشنهادی را وارد کنید...'
            }),
            
            'content': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'توضیحات خود را در اینجا بنویسید...',
                'rows': 4 
            }),
        }