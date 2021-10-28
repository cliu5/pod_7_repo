from django.shortcuts import render

# Create your views here.


def hello(request):
    if request.method == 'GET':
        return render(request=request, template_name='hello.html')


def hello_name(request, name):
    if request.method == 'GET':
        return render(request=request, template_anme='hello_name.html', context={'name': name})
