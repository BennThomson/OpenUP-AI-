from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomUserCreationForm, CustomUserLoginForm, user_edit_form
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.conf import settings


def user_register_view(request):
    request.META["title"] = "Register"
    if request.user.is_authenticated:
        return redirect("dashboard-main")

    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")
    context = {"form": form}
    return render(request, "Dashboard/registration/register.html", context)


def user_login_view(request):
    request.META["title"] = "Login"
    if request.user.is_authenticated:
        return redirect("dashboard-main")

    form = CustomUserLoginForm()
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            new_form = form.cleaned_data
            user = authenticate(email=new_form["email"], password=new_form["password"])
            if user:
                login(request, user)
                return redirect("dashboard-main")
            else:
                message = "Invalid credentials"
                return render(
                    request,
                    "Dashboard/registration/login.html",
                    {"form": form, "message": message},
                )
    context = {"form": form}
    return render(request, "Dashboard/registration/login.html", context)


def user_edit_view(request, id):
    user = CustomUser.objects.get(id=id)
    form = user_edit_form(instance=user)
    message = ""
    if request.method == "POST":
        form = user_edit_form(request.POST, instance=user)
        if form.is_valid():
            new_form = form.save(commit=False)
            print(new_form, "*" * 10)
            user.first_name = new_form.first_name
            user.last_name = new_form.last_name
            user.save()
            return redirect("dashboard-profile")
        else:
            message = "Invalid values were inputted"
    context = {"form": form, "message": message}
    return render(request, "Dashboard/profile.html")


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "registration/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")

    def form_valid(self, form):
        email = self.request.POST["email"]
        user = self.request.user
        try:
            user = user
        except StopIteration:
            user = None

        if user:
            context = {
                "user": user,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
                "protocol": "https" if self.request.is_secure() else "http",
                "domain": self.request.get_host(),
            }
            self.send_mail(
                subject_template_name=None,
                email_template_name=self.email_template_name,
                context=context,
                from_email=settings.EMAIL_HOST_USER,
                to_email=email,
                html_email_template_name="registration/password_reset_confirm.html",
            )
        return super().form_valid(form)

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
        generated_token=default_token_generator,
    ):
        print("Sending email", "*" * 20)
        email = self.request.POST["email"]

        plain_text_message = render_to_string(email_template_name, context)

        html_message = render_to_string(self.email_template_name, context)
        subject = "Password Reset Request"

        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_text_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[email],
        )
        email.attach_alternative(html_message, "text/html")

        email.send()


def user_logout_view(request):
    logout(request)
    return redirect("login")