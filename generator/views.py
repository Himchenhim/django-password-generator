from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length',14))

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*?~`|]['))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    password = ''
    for x in range(length):
        password += random.choice(characters)



    return render(request, 'generator/password.html',{'password':password})

def author(request):
    return render(request,'generator/author.html',{'name':'Dmytro Khimchenko', 'town':'Enerhodar'})

