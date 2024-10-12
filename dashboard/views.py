from django.shortcuts import render


def dashboard_main_view(request):
    return render(request, 'Dashboard/index.html')

def dashboard_community_view(request):
    return render(request, 'Dashboard/community-feed.html')

def dashboard_chatbot_view(request):
    return render(request, 'Dashboard/chatbot.html')

def dashboard_faq_view(request):
    return render(request, 'Dashboard/faq.html')

def dashboard_subscription_view(request):
    return render(request, 'Dashboard/manage-subscription.html')

