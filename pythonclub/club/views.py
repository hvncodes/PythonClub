from django.shortcuts import render
from .models import TopicType

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def posttypes (request):
    type_list=TopicType.objects.all()
    return render (request, 'club/types.html', {'type_list': type_list})