from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.template import RequestContext
from datetime import datetime
from django.conf import settings
from Main.apps import MainConfig

import json

# Create your views here.
def MainIndexView(request, *args, **kwargs):
    assert isinstance(request, HttpRequest)
    if settings.DEBUG:
        print(args, kwargs)
        print(request.user)
    context = {
        "language_code":settings.LANGUAGE_CODE,
        "page_title":MainConfig.name,
        "page_keywords":"Django, Python, Andreas Heine",
        "page_author":"Andreas Heine",
        'year':datetime.now().year,
        'main_nav_class':"active",
        'about_nav_class':"inactive",
    }
    return render(request=request, template_name="Main/index.html", context=context)

def MainAboutView(request, *args, **kwargs):
    assert isinstance(request, HttpRequest)
    if settings.DEBUG:
        print(args, kwargs)
        print(request.user)
    context = {
        "language_code":settings.LANGUAGE_CODE,
        "page_title":MainConfig.name,
        "page_keywords":"Django, Python, Andreas Heine",
        "page_author":"Andreas Heine",
        'year':datetime.now().year,
        'main_nav_class':"inactive",
        'about_nav_class':"active",
    }
    return render(request=request, template_name="Main/about.html", context=context)

def MainJsonDataView(request, *args, **kwargs):
    if settings.DEBUG:
        print(args, kwargs)
        print(request.user)
    if request.method=='POST':
        # check for json in request (contentType:"application/json")
        print(str(json.loads(request.body)))
        if request.is_ajax():
            context = {"toClient":"datafromdjango",}
            return JsonResponse(context)
        else:
            pass
    if request.method=='GET':
        context = {
            'time_value':datetime.now().strftime('%H:%M:%S'),
        }
        print(context)
        return JsonResponse(context)