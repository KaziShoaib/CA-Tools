import imp
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

import json
from django.http import JsonResponse

import calendar
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage

from django.db import IntegrityError
from .models import User, CA, ContactPerson, Report, Service
# Create your views here.


def integerConversion(intString):
    x = 0
    try:
        x = int(intString)
    except ValueError:
        pass
    return x


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("reports"))
        else:
            return render(request, "report/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "report/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("reports"))


@login_required(login_url='login')
def change_password_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        oldPassword = data.get("oldPassword")
        newPassword = data.get("newPassword")
        user = request.user
        if user.check_password(oldPassword):
            user.set_password(newPassword)
            user.save()
            return JsonResponse({"message": "success"}, status=201)
        return JsonResponse({"message": "failure"}, status=400)
    return render(request, "report/ChangePassword.html")


@login_required(login_url='login')
def AddUser(request):
    if request.method == 'POST':
        ca_id = int(request.POST['ca-name'])
        ca = CA.objects.get(pk=ca_id)
        username = request.POST['username']
        email = request.POST['email']
        password = User.objects.make_random_password()
        try:
            user = User.objects.create_user(username, email, password, ca=ca)
            user.save()
        except IntegrityError:
            return render(request, "report/AddUser.html", {
                "message": "Username already taken."
            })
        mailSubject = 'User Account Created for CA Info Tools'
        mailBody = f"User account has been create for username:{username}. Use {password} as password"
        mailRecipient = user.email
        msg = EmailMessage(mailSubject, mailBody, to=[mailRecipient])
        print(msg.send())
        # print(password)
        return HttpResponseRedirect(reverse('UserList'))

    cas = CA.objects.all()
    return render(request, "report/AddUser.html", {"cas": cas})


@login_required(login_url='login')
def UserList(request):
    users = filter(lambda u: not u.is_superuser, User.objects.all())
    return render(request, "report/UserList.html", {"users": users})


@login_required(login_url='login')
def report(request, report_id):
    report = Report.objects.get(pk=report_id)
    return render(request, "report/report.html", {
        "report": report
    })


@login_required(login_url='login')
def reports(request):
    reports = Report.objects.all()
    return render(request, "report/reports.html", {
        "reports": reports
    })


@login_required(login_url='login')
def submission(request):
    if request.method == 'POST':
        # print('hello')
        #ca_id = int(request.POST['ca-name'])
        ca = request.user.ca
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
        report = Report(ca=ca, month=month, year=year, submittedBy=request.user, classOneCertificates=classOneCertificates, classTwoCertificates=classTwoCertificates, classThreeCertificates=classThreeCertificates, eSigns=eSigns,
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


@login_required(login_url='login')
def CAList(request):
    cas = CA.objects.all()
    return render(request, "report/CAList.html", {"cas": cas})


@login_required(login_url='login')
def AddCA(request):
    if request.method == "POST":
        organizationName = request.POST['organization-name']
        organizationAddress = request.POST['organization-address']
        organizationWebsite = request.POST['organization-website']
        ca = CA(name=organizationName, address=organizationAddress,
                url=organizationWebsite)
        ca.save()

        # contactPersonName = request.POST['contact-person-name']
        # contactPersonDesignation = request.POST['contact-person-designation']
        # contactPersonEmail = request.POST['contact-person-email']
        # contactPersonPhone = request.POST['contact-person-phone']
        # contactPerson = ContactPerson(name=contactPersonName, designation=contactPersonDesignation,
        #                               email=contactPersonEmail, phone=contactPersonPhone, ca=ca)
        # contactPerson.save()

        # alternateContactPersonName = request.POST['alternate-contact-person-name']
        # alternateContactPersonDesignation = request.POST['alternate-contact-person-designation']
        # alternateContactPersonEmail = request.POST['alternate-contact-person-email']
        # alternateContactPersonPhone = request.POST['alternate-contact-person-phone']
        # alternateContactPerson = ContactPerson(name=alternateContactPersonName, designation=alternateContactPersonDesignation,
        #                                        email=alternateContactPersonEmail, phone=alternateContactPersonPhone, ca=ca)
        # alternateContactPerson.save()

        caPersonnelNames = request.POST.getlist('operations-personnel-name')
        caPersonnelDesignations = request.POST.getlist(
            'operations-personnel-designation')
        caPersonnelPhoneNumbers = request.POST.getlist(
            'operations-personnel-phone')
        caPersonnelEmails = request.POST.getlist('operations-personnel-email')
        for i in range(len(caPersonnelNames)):
            if caPersonnelNames[i] == '' and caPersonnelDesignations[i] == '' and caPersonnelPhoneNumbers[i] == '' and caPersonnelEmails[i] == '':
                continue
            caPeronnel = ContactPerson(
                name=caPersonnelNames[i], designation=caPersonnelDesignations[i], email=caPersonnelEmails[i], phone=caPersonnelPhoneNumbers[i], ca=ca)
            caPeronnel.save()
        return HttpResponseRedirect(reverse("CAList"))
    return render(request, "report/AddCA.html")
