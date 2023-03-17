import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from profiles.forms import RegisterUserForm
from profiles.forms import RegisterProfileForm
from profiles.models import Profile

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            User.objects.create(username=form.cleaned_data['username'],
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            logger.info(f"User email: {form.cleaned_data['email']}")
            logger.info(f"User password: {form.cleaned_data['password']}")
            return redirect("/")
    else:
        form = RegisterUserForm()

    return render(request, "register_user.html", {"form": form})

def register_profile(request):
    if request.method == 'POST':
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            Profile.objects.create(first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   age=form.cleaned_data['age']
                                   )
            return redirect('/')
    else:
        form = RegisterProfileForm()

    return render(request, 'register_profile.html', {'form': form})
