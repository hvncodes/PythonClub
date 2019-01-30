from django.shortcuts import render
from .models import Resources

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resources (request):
    resources_list=Resources.objects.all()
    return render (request, 'club/resources.html', {'resources_list': resources_list})