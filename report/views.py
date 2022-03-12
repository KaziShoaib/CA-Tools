from ast import Try
from asyncio.windows_events import NULL
from django.forms import NullBooleanField
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import calendar
from datetime import datetime

from .models import CA, ContactPerson, Report, Service
# Create your views here.


def integerConversion(intString):
    x = 0
    try:
        x = int(intString)
    except ValueError:
        pass
    return x


def report(request, report_id):
    report = Report.objects.get(pk=report_id)
    return render(request, "report/report.html", {
        "report": report
    })


def reports(request):
    reports = Report.objects.all()
    return render(request, "report/reports.html", {
        "reports": reports
    })


def submission(request):
    if request.method == 'POST':
        print('hello')
        ca_id = int(request.POST['ca-name'])
        ca = CA.objects.get(pk=ca_id)
        month = request.POST['month-name']
        year = int(request.POST['year'])
        classOneCertificates = integerConversion(
            request.POST['class-one-certificates'])
        classTwoCertificates = integerConversion(
            request.POST['class-two-certificates'])
        classThreeCertificates = integerConversion(
            request.POST['class-three-certificates'])
        eSigns = integerConversion(request.POST['eSign-certificates'])
        lastInternalAuditDate = request.POST['internal-audit-date']
        lastExternalAuditDate = request.POST['external-audit-date']
        campaign = request.POST['campaign-activity']
        comments = request.POST['comments']
        report = Report(ca=ca, month=month, year=year, classOneCertificates=classOneCertificates, classTwoCertificates=classTwoCertificates, classThreeCertificates=classThreeCertificates, eSigns=eSigns,
                        lastInternalAuditDate=lastInternalAuditDate if lastInternalAuditDate else None, lastExternalAuditDate=lastExternalAuditDate if lastExternalAuditDate else None, campaign=campaign, comments=comments)
        report.save()

        digitalServiceNames = request.POST.getlist('digital-service-name')
        digitalServiceOrgnaizationNames = request.POST.getlist(
            'digital-service-organization-name')
        digitalServiceElectronicSignatureNumbers = request.POST.getlist(
            'digital-service-electronic-signature-number')
        for i in range(len(digitalServiceNames)):
            if digitalServiceNames[i] == '' and digitalServiceOrgnaizationNames[i] == '' and digitalServiceElectronicSignatureNumbers[i] == '':
                continue
            digitalService = Service(serviceName=digitalServiceNames[i], organizationName=digitalServiceOrgnaizationNames[i],
                                     totalDigitalCertificates=integerConversion(digitalServiceElectronicSignatureNumbers[i]))
            digitalService.report = report
            digitalService.save()

        return HttpResponseRedirect(reverse('reports'))

    cas = CA.objects.all()
    return render(request, "report/submission.html", {
        "months": [(calendar.month_name[i], calendar.month_name[i]) for i in range(1, 13)],
        "years": [i for i in range(datetime.now().year-1, datetime.now().year+3)],
        "cas": cas
    })


def CAList(request):
    cas = CA.objects.all()
    return render(request, "report/CAList.html", {"cas": cas})


def AddCA(request):
    if request.method == "POST":
        organizationName = request.POST['organization-name']
        organizationAddress = request.POST['organization-address']
        organizationWebsite = request.POST['organization-website']
        ca = CA(name=organizationName, address=organizationAddress,
                url=organizationWebsite)
        ca.save()

        contactPersonName = request.POST['contact-person-name']
        contactPersonDesignation = request.POST['contact-person-designation']
        contactPersonEmail = request.POST['contact-person-email']
        contactPersonPhone = request.POST['contact-person-phone']
        contactPerson = ContactPerson(name=contactPersonName, designation=contactPersonDesignation,
                                      email=contactPersonEmail, phone=contactPersonPhone, ca=ca)
        contactPerson.save()

        alternateContactPersonName = request.POST['alternate-contact-person-name']
        alternateContactPersonDesignation = request.POST['alternate-contact-person-designation']
        alternateContactPersonEmail = request.POST['alternate-contact-person-email']
        alternateContactPersonPhone = request.POST['alternate-contact-person-phone']
        alternateContactPerson = ContactPerson(name=alternateContactPersonName, designation=alternateContactPersonDesignation,
                                               email=alternateContactPersonEmail, phone=alternateContactPersonPhone, ca=ca)
        alternateContactPerson.save()
        return HttpResponseRedirect(reverse("CAList"))

    return render(request, "report/AddCA.html")
