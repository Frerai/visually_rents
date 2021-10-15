from django.shortcuts import render  # Used to render/show/display pages


def home(request):
    """Displaying home page."""
    return render(request, 'home.html')  # A context object, third argument, is not passed in here, because no data is
#  to be displayed on the Home Page.

