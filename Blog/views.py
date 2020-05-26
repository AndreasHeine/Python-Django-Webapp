from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.conf import settings
from Blog.apps import BlogConfig

# Create your views here.
def BlogIndexView(request, *args, **kwargs): # *args, **kwargs
    assert isinstance(request, HttpRequest)
    if settings.DEBUG:
        print(args, kwargs)
        print(request.user)
    context = {
        "language_code":settings.LANGUAGE_CODE,
        "page_title":BlogConfig.name,
        "page_keywords":"Django, Python, Andreas Heine",
        "page_author":"Andreas Heine",
        'year':datetime.now().year,
        'blog_nav_class':"active",
    }
    return render(request=request, template_name="Blog/index.html", context=context)