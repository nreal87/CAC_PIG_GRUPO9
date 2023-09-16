from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

def styles(request):
    context = {}
    return render(request, "assets/css/styles.css", context)