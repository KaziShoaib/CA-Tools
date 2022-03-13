from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CA(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=300)
    url = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    ca = models.ForeignKey(
        'CA', on_delete=models.CASCADE, related_name='users', blank=True, null=True)


class ContactPerson(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    ca = models.ForeignKey('CA', on_delete=models.CASCADE,
                           related_name='contactPersons')


class Report(models.Model):
    month = models.CharField(max_length=10)
    year = models.IntegerField()
    ca = models.ForeignKey(
        'CA', on_delete=models.CASCADE, related_name='reports')
    submittedBy = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True)
    submittedAt = models.DateField(auto_now=True)
    classOneCertificates = models.IntegerField(blank=True)
    classTwoCertificates = models.IntegerField(blank=True)
    classThreeCertificates = models.IntegerField(blank=True)
    eSigns = models.IntegerField(blank=True)
    lastInternalAuditDate = models.DateField(blank=True, null=True)
    lastExternalAuditDate = models.DateField(blank=True, null=True)
    campaign = models.TextField(blank=True)
    comments = models.TextField(blank=True)


class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    organizationName = models.CharField(max_length=100)
    totalDigitalCertificates = models.IntegerField()
    report = models.ForeignKey(
        'Report', on_delete=models.CASCADE, related_name='services')
