from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import ProfileModel
from .models import saved_documents, Billing_model
from .chat_maker import chat_maker


@login_required
def dashboard_main_view(request):
    user = request.user
    profile = ProfileModel.objects.get(user=user)
    try:
        documents = saved_documents.objects.filter(user=user)
    except saved_documents.DoesNotExist:
        documents = None

    context = {
        "profile": profile,
        "documents": documents,
    }
    return render(request, "Dashboard/index.html", context=context)


@login_required
def dashboard_community_view(request):
    request.META["title"] = "Community"
    return render(request, "Dashboard/community-feed.html")


@login_required
def dashboard_chatbot_view(request):
    request.META["title"] = "Chatbot"
    question = request.POST.get("question")
    answer = None
    if question is not None:
        try:
            answer = chat_maker(question)
        except SyntaxError as e:
            pass

    if answer is not None:
        context = {
            "question": question,
            "answer": answer,
        }
    else:
        context = {
            "message": "Try again",
        }
    return render(request, "Dashboard/chatbot.html", context=context)


@login_required
def dashboard_profile_view(request):
    request.META["title"] = "Profile"
    payments = Billing_model.objects.filter(user=request.user)
    context = {
        "payments": payments,
    }
    return render(request, "Dashboard/profile.html", context=context)


@login_required
def dashboard_subscription_view(request):
    request.META["title"] = "Subscription"
    return render(request, "Dashboard/manage-subscription.html")
