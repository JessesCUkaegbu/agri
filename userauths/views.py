from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import re
from .adapter import MyGoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView
from django.contrib.auth import logout as auth_logout

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        # Get the form inputs using the HTML name attributes
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        # Basic input validation
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'userauths/sign_up.html', {'no_header': True})

        # Email format validation
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            messages.error(request, "Please enter a valid email address.")
            return render(request, 'userauths/sign_up.html', {'no_header': True})

        # Password complexity check
        if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[A-Za-z]', password):
            messages.error(request, "Password must be at least 8 characters long and contain both letters and numbers.")
            return render(request, 'userauths/sign_up.html', {'no_header': True})

        # Check if the user already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "User already exists.")
            return render(request, 'userauths/sign_up.html', {'no_header': True})

        # Create the user
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Hey, your account was created successfully")
        return redirect('login')

    return render(request, "userauths/sign_up.html", {'no_header': True})


def user_login(request):
    if request.method == 'POST':
        # Get the form inputs using the HTML name attributes
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        # Basic input validation
        if not username or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'userauths/login.html', {'no_header': True})

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('index')  # Redirect to the home page after successful login
        else:
            # If authentication fails, render the login form with an error message
            messages.error(request, "Invalid username or password")
            return render(request, 'userauths/login.html', {"fname": username, 'no_header': True})

    return render(request, "userauths/login.html", {'no_header': True})


# def logout_view(request):
#     logout(request)
#     messages.success(request, "You have successfully logout")
#     return redirect("login")

def logout_view(request):
    auth_logout(request)
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('login') 

class MyGoogleLoginView(OAuth2LoginView):
    adapter_class = MyGoogleOAuth2Adapter