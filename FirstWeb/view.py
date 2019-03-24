from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse("goodbye world ! ")

 
def htmltest(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'htmltest.html', context)