from django.shortcuts import render, get_object_or_404
from .models import Resources, Events
from .forms import EventForm

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resources (request):
    resources_list=Resources.objects.all()
    return render (request, 'club/resources.html', {'resources_list': resources_list})

def getevents (request):
    event_list=Events.objects.all()
    return render(request, 'club/events.html', {'event_list': event_list})

def eventdetail(request, id):
    detail=get_object_or_404(Events, pk=id)
    context = {'detail': detail}
    return render(request, 'club/details.html', context=context)

#form view
def newevent(request):
    form=EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'club/newevent.html', {'form': form})