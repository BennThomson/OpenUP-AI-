from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_main_view(request):
    return render(request, 'Dashboard/index.html')

@login_required
def dashboard_community_view(request):
    return render(request, 'Dashboard/community-feed.html')

@login_required
def dashboard_chatbot_view(request):
    return render(request, 'Dashboard/chatbot.html')

@login_required
def dashboard_profile_view(request):
    return render(request, 'Dashboard/profile.html')

@login_required
def dashboard_subscription_view(request):
    return render(request, 'Dashboard/manage-subscription.html')

