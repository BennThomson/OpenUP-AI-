from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import render, redirect
from .forms import ContactForm

def MainPage(request):
    return render(request, 'Openup/light/index-two.html')

def contact_page(request):
    form = ContactForm()
    message = ''
    print('keldi')
    if request.method == 'POST':
        print('post ishladi')
        form = ContactForm(request.POST)
        if form.is_valid():
            print('malumotlar valid!')
            form.save()
            return redirect('contactPage')
        else:
            message = 'Some info was wrong'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Openup/light/contact.html', context)




