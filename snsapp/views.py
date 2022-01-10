from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import SnsModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupfunc(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'success': 'User added'})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'This user is already registered'})

    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    return render(request, 'login.html', {})

@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})
    