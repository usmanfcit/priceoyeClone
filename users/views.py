from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistrationForm, AccountUpdateForm
from .models import RoleChoices, Role, User


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.role, created = Role.objects.get_or_create(name=RoleChoices.CUSTOMER)
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

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error(None, "No account found with this email.")
                return render(request, "login.html", {"form": form})

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("homepage")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated successfully.")
            return redirect("my_account")
    else:
        form = AccountUpdateForm(instance=request.user)

    return render(request, "my_account.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
