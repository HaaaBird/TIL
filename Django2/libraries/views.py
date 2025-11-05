from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors':authors
    }
    return render(request, 'libraries/index.html', context)

def create_author(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass