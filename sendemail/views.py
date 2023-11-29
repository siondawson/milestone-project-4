from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# email app tutorial from https://learndjango.com/tutorials/django-email-contact-form-tutorial

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, "Email sent! We will respond as soon as possible")
            return redirect("success")
        
    template = "sendemail/email.html"
    context = {
        "form": form
    }
    return render(request, template, context)


def success(request):


    template = "sendemail/email_sent.html"
    context = {

    }

    return render(request, template, context)