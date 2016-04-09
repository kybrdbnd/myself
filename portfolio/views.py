from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'home.html',{})


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
            for key, value in form.cleaned_data.items():
                print(key, value)
                # redirect to a new URL:
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
