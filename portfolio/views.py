from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def home(request):
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
    return render(request, 'home.html', {'form': form})
