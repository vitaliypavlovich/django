import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect

from profiles.forms import RegisterForm

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create()
            logger.info(f"User email: {form.cleaned_data['email']}")
            logger.info(f"User password: {form.cleaned_data['password']}")
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

