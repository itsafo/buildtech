from django.shortcuts import render


# Create your views here.
def index(request):
    # One good old style of programming functions
    # Define your context variable, then render
    return render(request, "index.html", {})
