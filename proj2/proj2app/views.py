from django.shortcuts import render
def index(request):
    return render(request, 'home.html')

def aboutIndex(request):
    return render(request, 'about.html')
# Create your views here.
