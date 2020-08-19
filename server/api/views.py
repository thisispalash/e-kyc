from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DocumentSerializer, PersonSerializer
from .serializers import AllDocuments, AllPersons
from document.models import Document, Person

class DocViewSet(viewsets.ViewSet):
  ''' For url path(s) `api/docs/` and `api/docs/{pk}/`
  '''
  # v Uncomment if error
  # queryset = Document.objects.all().order_by('uploaded')

  def get_serializer_class(self):
    if self.detail: return DocumentSerializer
    return AllDocuments

  ''' router actions '''

  def list(self, req):
    queryset = Document.objects.all().order_by('uploaded')
    serializer = self.get_serializer_class()
    return Response(serializer.data)

  def create(self, req):
    pass

  def retrieve(self, req, pk=None):
    pass

  def update(self, request, pk=None):
    pass

  def partial_update(self, request, pk=None):
    pass

  def destroy(self, request, pk=None):
    pass

class PersonViewSet(viewsets.ViewSet):
  ''' For url path(s) `api/persons/` and `api/persons/{pk}/`
  '''
  queryset = Person.objects.all().order_by('created')

  def get_serializer_class(self):
    if self.detail: return PersonSerializer
    return AllPersons


  ''' router actions '''

  def list(self, req):
    queryset = Persons.objects.all().order_by('created')
    serializer = self.get_serializer_class()
    return Response(serializer.data)

  def create(self, req):
    pass

  def retrieve(self, req, pk=None):
    pass

  def update(self, request, pk=None):
    pass

  def partial_update(self, request, pk=None):
    pass

  def destroy(self, request, pk=None):
    pass


