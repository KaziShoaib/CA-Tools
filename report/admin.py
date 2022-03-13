from django.contrib import admin
from .models import User, CA, ContactPerson, Report, Service


class CAAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "ca")


# Register your models here.
admin.site.register(User)
admin.site.register(CA, CAAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Report)
admin.site.register(Service)
