from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.core.exceptions import ValidationError
from .models import User
import bcrypt

def index(request):
    rform = RegisterForm()
    lform = LoginForm()
    context = {
        'registerform' : rform,
        'loginform' : lform,
        'users' : User.objects.all()
    }
    return render(request, 'login_reg_app/index.html', context)

def register(request):
    rform = RegisterForm()
    lform = LoginForm()

    if request.method == 'POST':
        doneform = RegisterForm(request.POST)
        doneform.is_valid()
        try:
            doneform.clean_password2()
            instance = doneform.save(commit=False)
            instance.password = bcrypt.hashpw(instance.password.encode(), bcrypt.gensalt())
            print instance.password
            instance.save()
            request.session['user']=request.POST['email']
            context = {
                'users' : User.objects.all()
            }
            return redirect(reverse('fitness_app:index'))
        except ValidationError:
            context = {
                'registerform' : rform,
                'loginform' : lform,
                'errors' : doneform.errors,
                'users' : User.objects.all()
            }
            return render(request, 'login_reg_app/index.html', context)

def login(request):
    lform = LoginForm()
    rform = RegisterForm()

    if request.method == 'POST':
        doneform = LoginForm(request.POST)
        doneform.is_valid()
        try:
            doneform.checkMatch()
            request.session['user']=request.POST['email']
            context = {
                'users' : User.objects.all()
            }
            return redirect(reverse('fitness_app:index'))
        except ValidationError:
            context = {
                'registerform' : rform,
                'loginform' : lform,
                'errors' : doneform.errors,
                'user' : User.objects.get(email = request.session['user'])
            }
            return render(request, 'login_reg_app/index.html', context)

def logout(request):
    request.session.flush()
    return redirect(reverse('login_app:index'))