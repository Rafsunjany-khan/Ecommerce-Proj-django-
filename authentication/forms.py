from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.db import transaction


CHOICES = [
    ('Male', 'male'),
    ('Female', 'Female'),
]

# Regular User Registration Form
class UserRegistrationForm(UserCreationForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Testing Name', 'class': 'form-control', 'id': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email', 'class': 'form-control'}))
    gender = forms.ChoiceField(choices=CHOICES)
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'from-control'}))
    pass2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'from-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender', 'password1', 'password2']
         #widgets = {
          #   'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'from-control'}),
         #}

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        #self.fields['first_name'].widget.attrs['class'] = 'bg-warning'

    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        return user

