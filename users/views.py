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


