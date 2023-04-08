from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    data = {
        'students': students,
    }
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')