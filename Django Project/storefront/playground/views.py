from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request ->  response
#request handler

def say_hello(request):
    #Pull data from db
    #Transform
    #Send Email so on
    # return HttpResponse('Hello World')

    return render (request,'hello.html',{'name':'Bikash Chaudhary'})