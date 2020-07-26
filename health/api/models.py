from django.db import models

# New Models (just KYC)

DOCS = (
  ('PAS', 'passport'),
  ('DVL', 'driving licence'),
  ('PAN', 'pan card'),
  ('AAD', 'aadhar card')
)
FILES = (
  ('PDF', 'PDF'),
  ('IMG', 'Image')
)
LOC = (
  ('TEXT', 'File Processed'),
  ('FILE', 'File Stored'),
  ('BOTH', 'File Stored and Processed')
) # Needed?

class Document(models.Model):
  doctype = models.CharField(max_length=3, choices=DOCS)
  filetype = models.CharField(max_length=3, choices=FILES)
  hashcode = models.TextField() # To check for tempering - md5?
  uploaded = models.DateTimeField(auto_now_add=True) # Automatically adds datetime of creation
  
  access = models.CharField(max_length=4, choices=LOC)
  location = models.CharField(max_length=47)  
    # Another kind of access?
  # data :: data extracted post processing of the uploaded file
  # file :: location of file
  # blob :: file blob access in psql

  _person = models.ForeignKey(
    'Person',
    on_delete=models.CASCADE # TODO
  )

  class Meta:
    unique_together = ['doctype', '_person']

  def __str__(self):
    return "%s %s :: %s" % (doctype, uploaded, _person)

class Person(models.Model): # TODO : remove `blank=True` from all
  key = models.SlugField(blank=True) # unique identifier for user reference

  name = models.CharField(max_length=47,blank=False)
  dob = models.DateField()
  permanent = models.TextField()
  current = models.TextField()
  # img :: Blob? Image file from docs or selfie?

  iden_type = models.CharField(max_length=3, choices=DOCS, blank=True)
  iden_value = models.TextField(blank=True)

  created = models.DateTimeField(auto_now_add=True) # Automatically adds datetime of creation
  docs = models.ManyToManyField(Document)
  links = models.ManyToManyField('self')

  def __str__(self):
    return '%s :: %s' % (name, dob)