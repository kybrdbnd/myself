from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm, HireForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HireForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sender = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            name = form.cleaned_data.get("full_name")
            phone = form.cleaned_data.get("phone")
            subject = "Hire Message"
            mail_message = " %s sends this message %s having phone no. %s \n\n Email id: %s" % \
                           (name, message, phone, sender)
            from_email = sender
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(subject,
                      mail_message,
                      from_email,
                      to_email,
                      fail_silently=False)
            for key, value in form.cleaned_data.items():
                print(key, value)
            messages.success(request, 'Mail send successfully')
            return HttpResponseRedirect('/')

    else:
        form = HireForm()
        return render(request, 'home.html', {'form': form})


def about(request):
    return render(request, 'about.html', {})


def skill(request):
    return render(request, 'skill.html', {})


def education(request):
    return render(request, 'education.html', {})


def work(request):
    return render(request, 'work.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sender = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            name = form.cleaned_data.get("full_name")
            subject = "Contact Message"
            mail_message = " %s sends this message %s \n\n Email id: %s" % \
                           (name, message, sender)
            from_email = sender
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(subject,
                      mail_message,
                      from_email,
                      to_email,
                      fail_silently=False)
            for key, value in form.cleaned_data.items():
                print(key, value)
            messages.success(request, 'Mail send successfully')
            return HttpResponseRedirect('/contact/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
