from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='نام', max_length=255, required=True)
    last_name = forms.CharField(label='نام‌خانوادگی', max_length=255, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email']


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        
        if self.cleaned_data.get("password1"):
            user.set_password(self.cleaned_data.get("password1"))
            
        if commit:
            user.save()
            profile = user.profile
            profile.first_name = self.cleaned_data.get('first_name')
            profile.last_name = self.cleaned_data.get('last_name')
            profile.save()

        return user























