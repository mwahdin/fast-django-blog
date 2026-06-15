from django import forms


class ContactForm(forms.Form):
    fullName = forms.CharField(label="full name", max_length=100)
    email = forms.EmailField(label="email")
    subject = forms.CharField(label="subject", max_length=200)
    message = forms.CharField(
        label="message",
        widget=forms.Textarea(attrs={"placeholder": "Enter your request"}),
    )
