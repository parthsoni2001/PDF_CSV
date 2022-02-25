from pyexpat import model
from attr import field
from django import forms
from .models import UploadPDF
from django.forms import ClearableFileInput


class UploadPDFForm(forms.ModelForm):

    class Meta:
        model = UploadPDF
        fields = ['upload']
        widgets = {'upload': ClearableFileInput(attrs={'multiple': True}),}