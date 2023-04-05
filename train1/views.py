from django.shortcuts import render

# Create your views here.
def boggie(request):
    return render(request, 'boggie.html')