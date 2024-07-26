# fire/forms.py

from django import forms
from django.db import models
from .models import TransientHouse, Room
from django.contrib.auth.models import User
from .models import Profile

class TransientHouseForm(forms.ModelForm):
    class Meta:
        model = TransientHouse
        fields = ['name', 'description', 'price_per_night', 'capacity', 'location', 'images']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price_per_night': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'email', 'first_name', 'last_name', 'phone_number', 'address']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'specification']
