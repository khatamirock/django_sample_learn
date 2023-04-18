from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


def mamas(request):
    return HttpResponse('maama kmn acoo')


def gen2(request):
    return render(request, 'gen2.html')

# create a function the receives an int. and return the square of that int.


def square(request, num):
    return HttpResponse(num**2)
