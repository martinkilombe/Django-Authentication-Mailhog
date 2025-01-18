from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.urls import reverse



from .models import *

@login_required
def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html')

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, "Passwords don't match!")
            return redirect('register')
            
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address!")
            return redirect('register')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')
            
        # Validate password strength
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, "\n".join(e.messages))
            return redirect('register')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login_page')
    
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('login_page')


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            # Generate token and uid
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Build reset URL
            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Email content
            email_template = 'password_reset_email.html'
            context = {
                'user': user,
                'reset_url': reset_url,
                'site_name': 'BumpAi',
            }
            email_html = render_to_string(email_template, context)
            
            try:
                send_mail(
                    'Password Reset Request',
                    'Please click the link to reset your password',
                    'noreply@bumpai.com',
                    [email],
                    html_message=email_html,
                    fail_silently=False,
                )
                return redirect('password_reset_done')
            except BadHeaderError:
                messages.error(request, "Invalid header found in email")
                
        # Always show success to prevent email enumeration
        return redirect('password_reset_done')
        
    return render(request, 'password_reset.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            
            if password == password2:
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successful!')
                return redirect('login_page')
            else:
                messages.error(request, "Passwords don't match!")
        
        return render(request, 'password_reset_confirm.html')
    else:
        messages.error(request, 'Password reset link is invalid or has expired!')
        return redirect('login_page')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')