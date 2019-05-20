from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # display blank registration form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST["password1"])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))

    context = {"form": form}
    return render(request, "users/register.html", context)
