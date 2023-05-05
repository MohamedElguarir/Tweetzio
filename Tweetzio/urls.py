from django.contrib import admin
from django.urls import path, include
"""
current urls.py in main project

def index(request):
    return render(request, 'TwitterSentiments/index.html')


def about(request):
    return render(request, 'TwitterSentiments/about.html')


def contact(request):
    return render(request, 'TwitterSentiments/contact.html')

def login(request):
    return render(request, 'TwitterSentiments/login.html')

def signup(request):
    return render(request, 'TwitterSentiments/signup.html')

def passwordreset(request):
    return render(request, 'TwitterSentiments/resetpassword.html')


def analyse(request):
    return render(request, 'TwitterSentiments/analyse.html')

def results(request):
    return render(request, 'TwitterSentiments/result.html')


"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TwitterSentiments.urls')),
]

