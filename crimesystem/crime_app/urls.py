from django.urls import path
from crime_app.views import *

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("cv/", casesview, name="cv"),
]