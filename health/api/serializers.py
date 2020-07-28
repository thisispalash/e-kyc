from rest_framework import serializers
from . import models


class MessageListField(serializers.ListField):
  child = serializers.CharField()
  allow_empty = True


class PersonSerializer(serializers.Serializer):
  name = serializers.CharField()
  current = serializers.CharField()
  dob = serializers.DateField()
  created = serializers.DateTimeField(read_only=True)

  links = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='name' 
  )
  docs = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='doctype'
  )

class DocumentSerializer(serializers.ModelSerializer):
  _person = serializers.StringRelatedField()
  class Meta:
    model = models.Document
    fields = ['doctype', '_person', 'uploaded']

# class LoginSerializer(serializers.ModelSerializer):
#   messages = MessageListField()
#   class Meta:
#     model = models.Login
#     fields = ['username', 'usertype', 'linked']