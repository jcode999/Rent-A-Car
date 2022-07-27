
from django.shortcuts import render, redirect
from account.models import Account
from .forms import LogInForm, RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request, username):
    user = Account.objects.get(username=username)
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard.html', {'user': user})
    else:
        return render(request, 'invalidpage.html')


def logIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account:dashboard", username)

        else:
            messages.error(
                request, f"Invalid Username or Password")

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


def log_out(request):
    logout(request)
    messages.success(request, ("You are logged out"))
    return redirect('account:login')
