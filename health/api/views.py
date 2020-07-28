from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views import View
from django.views.generic.edit import FormView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from . import models, forms, serializers


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



# class LoginView(FormView): # TODO: OAuth w/ REST
#   '''
#   Login view to access db data
#   '''
  
#   template_name = 'login.html'
#   success_url = 'api.html'
#   form_class = forms.LoginForm
#   context = {
#     'form': form_class()
#   }

#   def get(self, req):
#     return render(req, self.template_name, self.context)

#   def form_valid(self, form): # ie, called if form.is_valid == True
#     data = form.cleaned_data
#     messages = []
#     try:
#       user = models.Login.objects.get(username=data['username'])
#     except models.Login.DoesNotExist:
#       messages.append('User not found')
#       serializer = serializers.LoginSerializer(messages)
#       return JsonResponse(serializer.errors, safe=False, status=404)
    
#     if user.password == data['password']:
#       return super(LoginView,self).form_valid(form)
#     else:
#       self.context.form = forms.LoginForm()
#       return render(req, self.template_name, self.context)
  
#   def form_invalid(self, form): # ie, called if form.is_valid == False
#     pass

