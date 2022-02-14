from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'last_name', 'password1', 'password2']


