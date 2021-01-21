from django import forms
from django.contrib.auth.models import User
from apps.kmanalisis.models import CSV

class DocumentForm(forms.ModelForm):
    class Meta:
        model = CSV
        fields = ('file',)