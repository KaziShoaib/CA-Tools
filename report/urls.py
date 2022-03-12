from django.urls import path
from . import views


urlpatterns = [
    path("", views.reports, name='reports'),
    path("report/<int:report_id>", views.report, name="report"),
    path("submission", views.submission, name='submission'),
    path("CAList", views.CAList, name="CAList"),
    path("AddCA", views.AddCA, name="AddCA")
]
