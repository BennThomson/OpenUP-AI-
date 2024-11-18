from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import FaqsModel
from users.models import ProfileModel
from .essay_checker import check_essay


def MainPage(request):
    faqs = FaqsModel.objects.all()
    context = {"faqs": faqs}
    return render(request, "Openup/light/index-two.html", context)


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
    context = {}
    task = request.POST.get('inlineRadioOptions')
    person = ProfileModel.objects.get(user=request.user)
    try:
        text = request.POST.get("text")
    except Exception as e:
        text = ""

    text = f"\"{text}\""
    len_of_text = len(text.split(' '))
    print(len_of_text)
    yes_words = person.available_words > len_of_text

    if text and yes_words:
        print('ishladi')
        try: 
            result = check_essay(text, task)
        except Exception as e:
            result = ()
        if result:
            person.available_words -= len_of_text
            person.save()
            
            # info
            task_response = result['criteria']['Task Achievement']
            band_range_tr = task_response['band_range']
            coherence_response = result['criteria']['Coherence and Cohesion']
            band_range_cr = coherence_response['band_range']
            lexical_response = result['criteria']['Lexical Resource']
            band_range_lr = lexical_response['band_range']
            grammatical_response = result['criteria']['Grammatical Range and Accuracy']
            band_range_gr = grammatical_response['band_range']
            overall_band_score = result['output_format']['overall_band_score']
            improvement_suggestions = result['output_format']['improvement_suggestions']

            context = {
                'text': text,
                'results': result,
                # results
                'task_response': task_response,
                'band_range_tr': band_range_tr,
                'coherence_response': coherence_response,
                'band_range_cr': band_range_cr,
                'lexical_response': lexical_response,
                'band_range_lr': band_range_lr,
                'grammatical_response': grammatical_response,
                'band_range_gr': band_range_gr,
                'overall_band_score': overall_band_score,
                'improvement_suggestions': improvement_suggestions,
            }
    return render(request, "Openup/light/index-two.html", context)