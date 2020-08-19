from django.db import models

# Create your models here.

DOCTYPE = [
  ('PASS', 'Passport'),
  ('DVL', 'driving licence'),
  ('PAN', 'pan card'),
  ('AADH', 'aadhar card'),
]

FILETYPE = [
  ('PDF', 'PDF document'),
  ('PNG', 'PNG image'),
  ('JPG', 'JPG/JPEG image'),
  # TODO Check for other formats (TIFF, BMP) #
]

# { pass:{ pdf: base64, png: base64 }, dvl:{ pdf: base64, png: base64 }, }

class Document(models.Model):
  key = models.SlugField(blank=True) # unique identifier for user reference
  uploaded = models.DateTimeField(auto_now_add=True) # Automatically adds datetime of creation
  filehash = models.TextField() # To check for tempering - md5?

  doctype = models.CharField(max_length=4, choices=DOCTYPE)
  filetype = models.CharField(max_length=3, choices=FILETYPE)
  location = models.SlugField(blank=False) # location of file  
    # Another kind of access?
  # data :: data extracted post processing of the uploaded file
  # file :: location of file
  # blob :: file blob access in psql

  iden = models.CharField(max_length=20) # The unique ID of the document

  person = models.ForeignKey(
    'Person',
    on_delete=models.CASCADE, # TODO check out RESTRICT
    related_name='docs' # for reverse-relationship
  )

  def __str__(self):
    return "%s [key :: %s]" % (self.doctype, self.key)


class Person(models.Model):
  key = models.SlugField(blank=True) # unique identifier for user reference
  created = models.DateTimeField(auto_now_add=True) # Automatically adds datetime of creation

  name = models.CharField(max_length=47,blank=False)
  dob = models.DateField()
  address = models.TextField()

  links = models.ForeignKey(
    'self',
    on_delete=models.CASCADE # TODO check out RESTRICT
  )

  def __str__(self):
    return '%s [%s]' % (self.name, self.dob)
