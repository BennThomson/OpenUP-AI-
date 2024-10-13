from django.shortcuts import render

def user_register_view(request):
    return render(request, 'Dashboard/registration/register.html')

def user_login_view(request):
    return render(request, 'Dashboard/registration/login.html')



