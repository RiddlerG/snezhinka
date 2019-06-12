from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import LoginForm, RegisterForm
from landing.tokens import account_activation_token
from users.models import User


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()

        context = {
            'login_form': login_form,
        }

        return render(request, 'users/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            if request.recaptcha_is_valid:
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')

                if not login_form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(0)

                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('/')

        context = {
            'login_form': login_form,
        }

        return render(request, 'users/login.html', context)


class RegisterView(View):
    def get(self, request):
        reg_form = RegisterForm()

        context = {
            'reg_form': reg_form,
        }

        return render(request, 'users/register.html', context)

    def post(self, request):
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid():
            if request.recaptcha_is_valid:
                new_user = reg_form.save(commit=False)
                new_user.is_active = False
                new_user.email = reg_form.cleaned_data.get('username')
                new_user.username = reg_form.cleaned_data.get('username')
                password = reg_form.cleaned_data.get('password1')
                new_user.set_password(password)
                new_user.save()
                
                try:
                    current_site = get_current_site(request)
                    mail_subject = 'Подтверждение почты'
                    message = render_to_string('users/account_activate_message.html', {
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                        'token': account_activation_token.make_token(new_user),
                    })
                    to_email = new_user.email
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                except:
                    return render(request, 'users/account_activate_error.html')
                else:
                    return render(request, 'users/account_activate_done.html')

        context = {
            'reg_form': reg_form,
        }

        return render(request, 'users/register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64).decode())
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/account_activate_complete.html')
    else:
        return render(request, 'users/account_activate_old.html')


def mylogout(request):
    logout(request)
    return redirect('login')


class ProfileView(View):
    def get(self, request):

        context = {
        }

        return render(request, 'users/profile.html', context)

    def post(self, request):
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid():
            if request.recaptcha_is_valid:
                new_user = reg_form.save(commit=False)
                new_user.is_active = False
                new_user.email = reg_form.cleaned_data.get('username')
                new_user.username = reg_form.cleaned_data.get('username')
                password = reg_form.cleaned_data.get('password1')
                new_user.set_password(password)
                new_user.save()
                
                try:
                    current_site = get_current_site(request)
                    mail_subject = 'Подтверждение почты'
                    message = render_to_string('users/account_activate_message.html', {
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                        'token': account_activation_token.make_token(new_user),
                    })
                    to_email = new_user.email
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                except:
                    return render(request, 'users/account_activate_error.html')
                else:
                    return render(request, 'users/account_activate_done.html')

        context = {
            'reg_form': reg_form,
        }

        return render(request, 'users/register.html', context)


class UserOrdersView(View):
    def get(self, request):

        context = {
        }

        return render(request, 'users/orders.html', context)