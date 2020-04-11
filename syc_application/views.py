from django.shortcuts import render
from .models import script


# Create your views here.
def excute(request):
    scripts = script.objects.all()
    return render(request, "excute.html", {"scripts": scripts})
