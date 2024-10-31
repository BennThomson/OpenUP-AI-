from django.shortcuts import render

def MainPage(request):
    return render(request, 'Openup/light/index-two.html')

def contact_page(request):
    return render(request, 'Openup/light/contact.html')




