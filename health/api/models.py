from django.db import models

# New Models (just KYC)

class Document(models.Model):
  DOCS = (
    ('PASS', 'passport'),
    ('DVLS', 'driving licence')
  ); doctype = models.CharField(max_length=4, choices=DOCS)
  FILES = (
    ('PDF', 'PDF'),
    ('IMG', 'Image')
  ); filetype = models.CharField(max_length=3, choices=FILES)
  LOC = (
    ('TEXT', 'File Extracted'),
    ('FILE', 'File Stored')
  ); access = models.CharField(max_length=4, choices=LOC)
  
  location = models.CharField(max_length=47)
  hashcode = models.TextField()
  
  _person = models.ForeignKey(
    'Person',
    on_delete=models.CASCADE # TODO
  )


class Person(models.Model):
  name = models.CharField(max_length=47,blank=False)
  dob = models.DateField()
  permanent = models.TextField()
  current = models.TextField()

  docs = models.ManyToManyField(Document)
  links = models.ManyToManyField('self')
