from django.forms import ModelForm
from django.db import models
from django import forms
from .models import Person, Servant


class AddForm(ModelForm):
    class Meta:
        model = Person
        fields = ['author','categoryType', 'name', 'year', 'cash', 'img']

class AddFormServant(ModelForm):
    class Meta:
        model = Servant
        fields = ['author', 'name', 'year', 'cash']