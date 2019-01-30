from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Call, Type
from .forms import RegisterForm


def index(request):
    """
    Our index view function that allows to either list all calls
    of register a new call.
    """
    return render(request, 'calls/index.html')
    
def register(request):
    """
    Our view function to register an new call in the database.
    """
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
                        
            duration = form.cleaned_data['duration']
            type = form.cleaned_data['type']
            
            # save data in our database
            Call.objects.create(duration=duration, type=type)
            
            # redirect to a the list all calls url
            return HttpResponseRedirect(reverse('calls:list'))
            
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'calls/form.html', {'form': form})
    
def list(request):
    """
    The view function to list all the calls in the database.
    """
    call_list = Call.objects.all()
    context = {'call_list': call_list, }
    return render(request, 'calls/list.html', context)
    
