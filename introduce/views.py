from django.shortcuts import render
from introduce.models import AccessLog


# Create your views here.
def introduce(requetst):
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()

    return render(requetst, 'introduce.html')