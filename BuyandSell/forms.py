from django import forms
from django.contrib.auth.models import User
from .models import item,UserProfile


class SellForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']
