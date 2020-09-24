from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def dinner(request):
    menu = ['피자', '족발', '수육']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }
    return render(request, 'articles/dinner.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('name')
    context = {
        'message': message,
    }

    return render(request, 'articles/catch.html', context)