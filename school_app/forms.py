from django import forms
from .models import Teacher


class TeacherRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ('username', 'password1', 'password2', 'phone_number', 'subject', 'grade')
