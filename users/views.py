from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, RegistrationForm, AccountUpdateForm
from .models import RoleChoices, Role, User


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {"form": form}
        return render(self.request, "register.html", context)

    def post(self, request):
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.role, created = Role.objects.get_or_create(name=RoleChoices.CUSTOMER)
            form.save()
            messages.success(self.request, "Registration successful.")
            return redirect("login")
        else:
            form.add_error(None, "Invalid Data")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(self.request, "login.html", context)

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error(None, "No account found with this email.")
            user = authenticate(self.request, email=email, password=password)
            if user is not None:
                login(self.request, user)
                messages.success(self.request, "Login successful!")
                return redirect("homepage")
        else:
            form.add_error(None, "Invalid email or password.")
        return render(self.request, "login.html", {"form": form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = AccountUpdateForm(instance=self.request.user)
        return render(self.request, "profile.html", {"form": form})

    def post(self, request):
        form = AccountUpdateForm(self.request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Your account has been updated successfully.")
            return redirect("profile")
        return render(self.request, "profile.html", {"form": form})


class LogoutView(LoginRequiredMixin, View):
    def post(self, request):
        logout(self.request)
        messages.success(self.request, "Your account has been updated successfully.")
        return redirect("login")
