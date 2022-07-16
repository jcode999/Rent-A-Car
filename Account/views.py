
from django.shortcuts import render, redirect
from .forms import LogInForm, RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def logIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("account:dashboard")
        else:
            messages.error(
                request, f"Invalid email:{username} or password:{password}")

    form = AuthenticationForm()
    return render(request=request, template_name='registration/login.html', context={"login_form": form})


def registration(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("account:login")
    else:
        form = RegistrationForm()

    return render(response, 'registration/registration.html', {'registration_form': form})


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')