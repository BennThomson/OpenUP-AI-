from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import FaqsModel
from users.models import ProfileModel
from dashboard.models import content_artices_model
from .essay_checker import check_essay
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


def MainPage(request):
    faqs = FaqsModel.objects.all()
    articles = content_artices_model.objects.all()[:3]
    context = {
        "faqs": faqs,
        "articles": articles,
    }
    return render(request, "Openup/light/index-two.html", context)


def article_detail(request, pk):
    request.META["title"] = "Content detail"
    article = content_artices_model.objects.get(pk=pk)
    related_posts = content_artices_model.objects.filter(type=article.type).exclude(
        pk=article.pk
    )
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(article)
    hits = hit_count.hits
    hitcontext = context["hitcount"] = {"pk": hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits += 1
        hitcontext["hit_counted"] = hit_count_response.hit_counted
        hitcontext["hit_message"] = hit_count_response.hit_message
        hitcontext["total_hits"] = hits

    context = {
        "article": article,
        "related_articles": related_posts,
    }
    return render(request, "Openup/light/blog-details.html", context)


def contact_page(request):
    request.META["title"] = "Contact"
    form = ContactForm()
    message = ""
    print("keldi")
    if request.method == "POST":
        print("post ishladi")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("malumotlar valid!")
            form.save()
            return redirect("contactPage")
        else:
            message = "Some info was wrong"
    context = {"form": form, "message": message}
    return render(request, "Openup/light/contact.html", context)


def text_checker(request):
    task = request.POST.get("inlineRadioOptions")
    person = ProfileModel.objects.get(user=request.user)
    try:
        text = request.POST.get("text")
    except Exception as e:
        text = ""

    text = f'"{text}"'
    len_of_text = len(text.split(" "))
    yes_words = person.available_words > len_of_text

    if text:
        if yes_words:
            try:
                result = check_essay(text, task)
            except Exception as e:
                result = ()

            if result != "Incorrect text":
                if result:
                    person.available_words -= len_of_text
                    person.save()

                    # info
                    task_response = result["criteria"]["Task Achievement"]
                    band_range_tr = task_response["band_range"]
                    coherence_response = result["criteria"]["Coherence and Cohesion"]
                    band_range_cr = coherence_response["band_range"]
                    lexical_response = result["criteria"]["Lexical Resource"]
                    band_range_lr = lexical_response["band_range"]
                    grammatical_response = result["criteria"][
                        "Grammatical Range and Accuracy"
                    ]
                    band_range_gr = grammatical_response["band_range"]
                    overall_band_score = result["output_format"]["overall_band_score"]
                    improvement_suggestions = result["output_format"][
                        "improvement_suggestions"
                    ]
                    try:
                        words = result["words"]
                    except Exception as e:
                        words = []

                    context = {
                        "text": text,
                        "results": result,
                        # results
                        "task_response": task_response,
                        "band_range_tr": band_range_tr,
                        "coherence_response": coherence_response,
                        "band_range_cr": band_range_cr,
                        "lexical_response": lexical_response,
                        "band_range_lr": band_range_lr,
                        "grammatical_response": grammatical_response,
                        "band_range_gr": band_range_gr,
                        "overall_band_score": overall_band_score,
                        "improvement_suggestions": improvement_suggestions,
                        "words": words,
                    }
                else:
                    context = {"other_langauge": "Only English language is accepted!"}
            else:
                context = {
                    "Incorrect_text": "Only text is accepted.Double check it before sending!",
                }
        else:
            context = {
                "not_availability_of_words": "You have not enough words in your profile",
            }
    else:
        context = {"try_again": "Try again!"}
    return render(request, "Openup/light/index-two.html", context)
