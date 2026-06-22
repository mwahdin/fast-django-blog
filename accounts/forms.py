from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True, label="نام")
    last_name = forms.CharField(max_length=255, required=True, label="نام خانوادگی")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email']

    def save(self, commit=True):
        user = super().save(commit=commit)
        
        if commit:
            profile = user.profile
            profile.first_name = self.cleaned_data.get('first_name')
            profile.last_name = self.cleaned_data.get('last_name')
            profile.save()
            
        return user