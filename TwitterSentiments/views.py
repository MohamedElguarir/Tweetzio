from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import Classify
from . import TwitterAPI
from . import ContextSummary
from . import contactsend

# Create your views here.


def index(request):
  if request.method == 'GET':
    return render(request, 'TwitterSentiments/index.html')
        
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    contactsend.send_email(name, email, message)
    return render(request, 'TwitterSentiments/index.html', {'name': name})

def about(request):
    return render(request, 'TwitterSentiments/about.html')

def contact(request):
  if request.method == 'GET':
        return render(request, 'TwitterSentiments/contact.html')
        
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    contactsend.send_email(name, email, message)
    return render(request, 'TwitterSentiments/contact.html', {'name': name})
  
def login(request):

    return render(request, 'TwitterSentiments/login.html')

def logout(request):
    return render(request, 'TwitterSentiments/logout.html')

def signup(request):

    return render(request, 'TwitterSentiments/signup.html')

def passwordreset(request):

    return render(request, 'TwitterSentiments/resetpassword.html')

def analyse(request):
    return render(request, 'TwitterSentiments/analyse.html')
    

def result(request):
    if request.method == 'GET':
        return redirect('/analyse')

    context = {}
    if request.method == 'POST':

        positive_tweets = 0
        negative_tweets = 0
        neutral_tweets = 0

        query = request.POST['query']

        # retreive the tweets
        tweets = TwitterAPI.search_tweets(query, 20)
        
        # classify the tweets
        classified_tweets = Classify.classify_tweets(tweets)

        contextsummary = ContextSummary.context_summary(classified_tweets)
        print(context)

        for tweet in classified_tweets:
            if tweet['sentiment'] == 'Positive':
                positive_tweets += 1
            elif tweet['sentiment'] == 'Negative':
                negative_tweets += 1
            else:
                neutral_tweets += 1

        context = {
            'tweets': tweets,
            'query': query,
            'positive_tweets': positive_tweets,
            'negative_tweets': negative_tweets,
            'neutral_tweets': neutral_tweets,
            'contextsummary':contextsummary
        }

        return render(request, 'TwitterSentiments/results.html', context)