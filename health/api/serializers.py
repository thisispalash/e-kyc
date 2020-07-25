from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
  name = serializers.CharField()
  address = serializers.CharField()
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

# class DocumentSerializer(serializers.Serializer):
#   person = 
#   class Meta:
#     model = Document
#     fields = ['doctype', 'uploaded', 'hashcode', '_person']