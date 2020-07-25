from django import forms

from .models import Person

class UploadForm(forms.ModelForm):
  # doctype
  # file
  pass

class KYCForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = ['name', 'dob', 'permanent', 'current']
  pass