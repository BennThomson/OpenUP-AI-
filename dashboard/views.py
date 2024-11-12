from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import ProfileModel
from .models import saved_documents


@login_required
def dashboard_main_view(request):
    user = request.user
    profile = ProfileModel.objects.get(user=user)
    try:
        documents = saved_documents.objects.filter(user=user)
    except saved_documents.DoesNotExist:
        documents = None
        
    context = {
        'profile': profile,
        'documents': documents,
    }
    return render(request, 'Dashboard/index.html', context=context)

@login_required
def dashboard_community_view(request):
    request.META['title'] = 'Community'
    return render(request, 'Dashboard/community-feed.html')

@login_required
def dashboard_chatbot_view(request):
    request.META['title'] = 'Chatbot'
    return render(request, 'Dashboard/chatbot.html')

@login_required
def dashboard_profile_view(request):
    request.META['title'] = 'Profile'
    return render(request, 'Dashboard/profile.html')

@login_required
def dashboard_subscription_view(request):
    request.META['title'] = 'Subscription'
    return render(request, 'Dashboard/manage-subscription.html')

