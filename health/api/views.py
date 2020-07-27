from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views import View
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from . import models, serializers


@method_decorator(csrf_exempt, name='dispatch') # TODO : override dispatch to customise requests; maybe
class PersonView(View):
  model = models.Person

  def get(self, req): # get-all
    persons = models.Person.objects.all() # TODO privilige check
    serializer = serializers.PersonSerializer(persons, many=True)
    return JsonResponse(serializer.data, safe=False)

  def info(self, req, key): # doesn't work
    try:
      person = models.Person.objects.get(key=key)
    except models.Person.DoesNotExist:
      return HttpResponse(status=404)

      serializer = serializers.PersonSerializer(person)
      return JsonResponse(serializer.data)

  def post(self, req): # add-one
    data = JSONParser().parse(req)
    serializer = serializers.PersonSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
  
  def put(self, req, key): # update-one
    try:
      person = models.Person.objects.get(key=key)
    except models.Person.DoesNotExist:
      return HttpResponse(status=404)

    data = JSONParser().parse(req)
    serializer = serializers.PersonSerializer(person, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  def delete(self, req, key):
    try:
      person = models.Person.objects.get(key=key)
    except models.Person.DoesNotExist:
      return HttpResponse(status=404)

    person.delete()
    return HttpResponse(status=204)



@method_decorator(csrf_exempt, name='dispatch') # TODO : override dispatch to customise requests; maybe
class DocumentView(View):
  model = models.Document

  def get(self, req): # get-all
    docs = models.Document.objects.all() # TODO privilige check
    serializer = serializers.DocumentSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)

  def post(self, req): # add-one
    data = JSONParser().parse(req)
    serializer = serializers.DocumentSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
