from django.shortcuts import render

from .forms import UserForm

# Create your views here.


def index(request):
    usr = UserForm()
    return render(request, "blogs/index.html", {"usr": usr})
