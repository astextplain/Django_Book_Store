from django.shortcuts import render, HttpResponseRedirect

from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from App_Login.models import Profile
from App_Login.forms import profileform, SignUpForm

# Massages option
from django.contrib import messages


def sign_up(request):
    form = SignUpForm()  # object instace of class
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Sucessfully")
            return HttpResponseRedirect(reverse("App_Login:login"))
    return render(request, "App_Login\sign_up.html", context={"form": form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request, "App_Login\login.html", context={"form": form})


@login_required
def llogout(request):
    logout(request)
    messages.warning(request, "You are Logged Out")
    return HttpResponseRedirect(reverse('App_Shop:home'))


@login_required
# view function for profile
def user_profile(request):
    # Fetch the Profile instance associated with the logged-in user
    user1_profile = Profile.objects.get(user=request.user)

    # Initialize the form with the profile data
    form = profileform(instance=user1_profile)

    if request.method == "POST":
        # Process form submission with the same profile instance
        form = profileform(request.POST, instance=user1_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Sucessfully")
            form = profileform(instance=user1_profile)

    return render(request, "App_Login/change_profile.html", context={"form": form})
