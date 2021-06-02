from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def homePage(request):
    return render(request, 'homePage.html')

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Message from {form.cleaned_data['name']}"
            body = {
                'email address': f"Message from {form.cleaned_data['email']}",
                'message': form.cleaned_data['message'],
            }

            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'tonysoftlips@gmail.com', ['anthonyjelliman@gmail.com'])
            except:

                return render(request, 'contact.html', {'msg': 'Something went wrong! Please contact me +4530869358'})

            return render(request, 'contact.html', {'msg': "Thank you for the message \n I'll get back to you as soon as possible"})

    return render(request, 'contact.html',{'form': ContactForm()})

