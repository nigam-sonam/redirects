from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.cache import cache_page
#import pdb;pdb.set_trace()
#@cache_page(60,cache="special_cache")
def index(request):
    #import pdb;pdb.set_trace()
    return HttpResponse("Hello")

def bye(request):
    return HttpResponse("bye")

def login(request):
    return HttpResponse("login here")

def logout(request):
    return HttpResponse("logout....")
