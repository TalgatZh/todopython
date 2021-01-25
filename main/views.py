from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse('Hello world')

def third(request):
    return HttpResponse('This is page test3')

def test(request):
    return render(request,'test.html')
