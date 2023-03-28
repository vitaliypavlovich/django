import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from profiles.forms import RegisterUserForm, LoginForm
from profiles.forms import RegisterProfileForm
from profiles.models import Profile

from django.contrib.auth import logout, login, authenticate


logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/")
    else:
        form = RegisterUserForm()

    return render(request, "register_user.html", {"form": form})

def register_profile(request):
    if request.method == 'POST':
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            Profile.objects.create(user=request.user,
                                   first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   age=form.cleaned_data['age']
                                   )
            return redirect('/')
    else:
        form = RegisterProfileForm()

    return render(request, 'register_profile.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is None:
                return HttpResponse('BadRequest', status=400)
            login(request, user)
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")