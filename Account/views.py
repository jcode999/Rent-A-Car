
from django.shortcuts import render, redirect
from account.models import Account, Payment
from .forms import LogInForm, RegistrationForm, PaymentForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
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
            return redirect("account:dashboard")

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


def add_credit_card(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        cc_number = request.POST.get('cc_number')
        cc_expiry = request.POST.get('cc_expiry')
        cc_code = request.POST.get('cc_code')
        if request.user.is_authenticated:
            user = request.user
        card = Payment.create(cc_number, cc_expiry, cc_code, user)
        if form.is_valid():
            card.save()
            return redirect('account:dashboard')
    else:
        form = PaymentForm()
    return render(request, 'dashboard/paymentform.html', {'payment_form': form})


def update_info(request):
    user = request.user
    if request.method == 'GET':
        initial_dict = {'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        }
        form = UpdateUserForm(request.POST or None, initial=initial_dict)
        return render(request, 'dashboard/update_info.html', {'update_form': form, 'user': user, 'request_method': request.method})
    form = RegistrationForm()
    return render(request, 'dashboard/update_info.html', {'update_form': form, 'user': user, 'request_method': request.method})
