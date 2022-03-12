from django.db import models
import calendar

# Create your models here.


class CA(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=300)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"


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
