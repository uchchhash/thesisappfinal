from django.shortcuts import render
from .models import Area

# Create your views here.

def home(request):
    area = Area.objects.all()
    return render(request, 'area_app/home.html', {'area':area})
