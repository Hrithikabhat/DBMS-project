from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')
def signup(request):
    if request.method == "POST":
        voc = request.POST['voc']
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        conpass = request.POST['conpass']
        phoneno = request.POST['phoneno']
        address = request.POST['address']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if password != conpass:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        myuser = User.objects.create_user(name, email, password)
        myuser.name = name
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, 'home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    return render(request, 'signin.html')

def products(request):
    return render(request, 'products.html')

def nextpage(request):
    return render(request, 'products2.html')

