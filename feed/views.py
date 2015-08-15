from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import base64

# Create your views here.
def index(request):
    template = loader.get_template('feed/index.html')
    return HttpResponse(template.render()) # send the index

def feed(request, img_id):
    f = open("/home/ryan/{0}.png".format(img_id), "rb")
    b64 = base64.b64encode(f.read())
    f.close()
    return HttpResponse(b64) # send image

def warn(request):
    try:
        f = open("/home/ryan/warn" ,"r")
    except IOError:
        return HttpResponse() # nothing

    return HttpResponse("WARNING, SOMETHING CHANGED") # give warning

