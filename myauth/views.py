from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request, 'myauth/home.html')

def login(request):
    return render(request, 'myauth/file.html')

def remove_user_and_token(request):
  if 'token_cache' in request.session:
    del request.session['token_cache']

  if 'user' in request.session:
    del request.session['user']


def sign_out(request):
    remove_user_and_token(request)
    return HttpResponseRedirect(reverse('home'))