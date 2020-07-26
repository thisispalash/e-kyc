from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from . import models, serializers


# Create your views here.

# class PersonViewSet(viewsets.ModelViewSet):
#   queryset = models.Person.objects.all().order_by('dob')
#   serializer_class = serializers.PersonSerializer
  
@csrf_exempt
def person_list(req):
  """
  List all persons in DB or create new entry
  """

  if req.method == 'GET':
    persons = models.Person.objects.all() # TODO privilige check
    serializer = serializers.PersonSerializer(persons, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif req.method == 'POST':
    data = JSONParser().parse(req)
    serializer = serializers.PersonSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def person_info(req,key):
  """
  Retrieve, update or delete a code snippet.
  """
  try:
    person = models.Person.objects.get(key=key)
  except models.Person.DoesNotExist:
    return HttpResponse(status=404)

  if req.method == 'GET':
    serializer = serializers.PersonSerializer(person)
    return JsonResponse(serializer.data)

  elif req.method == 'PUT':
    data = JSONParser().parse(req)
    serializer = serializers.PersonSerializer(person, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif req.method == 'DELETE':
    person.delete()
    return HttpResponse(status=204)  


@csrf_exempt
def document_list(req):
  """
  List all documents in DB or create new entry
  """

  if req.method == 'GET':
    docs = models.Document.objects.all() # TODO privilige check
    serializer = serializers.DocumentSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif req.method == 'POST':
    data = JSONParser().parse(req)
    serializer = serializers.DocumentSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
