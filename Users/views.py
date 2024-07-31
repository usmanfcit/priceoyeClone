from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistrationForm
from .models import User


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            form.add_error(None, "Invalid Data")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
