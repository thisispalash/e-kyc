from django.db import models

# Create your models here.

class Document(models.Model):
  _id
  _customer # Customer::_id
  _category # KYC, Report, Claims, Diagnoses
  _doctype # [Passport, Licence,], [Data, Receipts,], [Bills, Prescriptions,], [Notes, Prescriptions,]
  _filetype # [PDF, img, hOCR, LaTeX,]
  size
  name
  location


class Customer(models.Model): # Insurer
  _id
  _data # Analytics of customer
  _info # Info::_id
  _doclist # [Document::_id,]
  _pref # Preferences::_id



class Info(models.Model): # Modularity for analytics
  _id
  _date # Last update
  _action # (CREATE,UPDATE,DELETE)
  _human # (Customer::_id,)
  _kyc # [KYC::_id,]
  _finance # [Bank::_id]
  name
  dob
  permanent # address
  current # address

class KYC(models.Model):
  _id
  _doc # Document::_id
  _type # [Passport,AADHAR,Licence,]
  number
  verify # Place to check the number; most online