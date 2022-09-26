from django.shortcuts import render

# Create your views here.
def introduce(requetst):
    return render(requetst, 'introduce.html')