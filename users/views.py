from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomUserLoginForm, user_edit_form
from django.contrib.auth import authenticate, login, logout

from .models import CustomUser


def user_register_view(request):
    print(request.POST)
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(form.cleaned_data)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'Dashboard/registration/register.html', context)

def user_login_view(request):
    form = CustomUserLoginForm()
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            new_form = form.cleaned_data
            user = authenticate(
                email=new_form['email'],
                password=new_form['password']
            )
            if user:
                login(request,user)
                return redirect('dashboard-main')
            else:
                message = 'Invalid credentials'
                return render(request, 'Dashboard/registration/login.html', {'form': form, 'message': message})
    context = {
        'form': form
    }
    return render(request, 'Dashboard/registration/login.html',context)

def user_logout_view(request):
    logout(request)
    return redirect('login')

def user_edit_view(request, id):
    user = CustomUser.objects.get(id=id)
    form = user_edit_form(instance=user)
    message = ''
    if request.method == 'POST':
        form = user_edit_form(request.POST, instance=user)
        if form.is_valid():
            new_form = form.save(commit=False)
            print(new_form, '*' * 10)
            user.first_name = new_form.first_name
            user.last_name = new_form.last_name
            user.save()
            return redirect('dashboard-profile')
        else:
            message = 'Invalid values were inputted'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Dashboard/profile.html')


from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.conf import settings

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'  # Use this if you have a specific email template
    success_url = reverse_lazy('password_reset_done')  # Redirect after successful email sending

    
    def form_valid(self, form):
        email = self.request.POST['email'] 
        # Get the user associated with the email in the form
        try:
            user = CustomUser.objects.get(email=email)
        except StopIteration:
            user = None 

        if user:
            # Prepare email context with uid, token, protocol, and domain
            context = {
                'user': user,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'protocol': 'https' if self.request.is_secure() else 'http',
                'domain': self.request.get_host(),
            }
            # Send the email using our custom `send_mail` function
            self.send_mail(
                subject_template_name=None,
                email_template_name=self.email_template_name,
                context=context,
                from_email=settings.EMAIL_HOST_USER,
                to_email=email,
                html_email_template_name='registration/password_reset_confirm.html'
            )
        return super().form_valid(form)



    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None, generated_token=default_token_generator):
        print('Sending email', '*' * 20)
        email = self.request.POST['email']

        plain_text_message = render_to_string(email_template_name, context)

        # Render HTML and plain text email templates
        html_message = render_to_string(self.email_template_name, context)
        subject = "Password Reset Request"
        
        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_text_message,  # Set the plain-text message
            from_email=settings.EMAIL_HOST_USER,
            to=[email],
        )

        email.attach_alternative(html_message, "text/html")

        # Send the email
        email.send()

