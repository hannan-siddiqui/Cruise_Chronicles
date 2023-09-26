from django.http import HttpResponse
from django.shortcuts import render
from manager.models import landingpagecontent


def homepage(request):

    landingpagecontentdata = landingpagecontent.objects.all()
    data = {
        'landingpagedata':landingpagecontentdata,
    }

    return render(request, "index.html", data)


def brand(request):
     branddata = brandpagecontent.objects.all()
    branddata = {
        'branddata':branddata,
    }
    return render(request, "brand.html", branddata)


def contact(request):
    return render(request, "contact.html")

def brandkoenigsig(request):
    return render(request,"brandkoenegsigg.html")
