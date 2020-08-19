from rest_framework import serializers
from document.models import Document, Person

class DocumentSerializer(serializers.ModelSerializer):
  ''' Fields accessible - doctype, file, uploaded, filehash, person
    file :: preferably a PDF file is sent, reconstructed through filetype and location
  '''

  class Meta:
    model=Document

class PersonSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
    model=Person
    fields=['key','name','dob','address','created','docs','links']