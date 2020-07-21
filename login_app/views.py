from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# Create your views here.

# elif username == '' or password == '':
#             message.info(request, 'Please enter these fields')

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, user)
            return redirect('/welcome/')
        else:
            messages.info(request, 'Username or Password incorrect')
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'login_app/index.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def createUser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        try: 
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully!")
                return redirect('index')
        except ValueError:
            messages.warning(request, "Please use safe credentials")
            return redirect('register')
    context = {'form': form}
    return render(request, 'login_app/create.html', context)

@login_required(login_url='index')
def welcome(request):
    user = request.user
    context = {'user':user}
    return render(request, 'login_app/welcome.html', context)
