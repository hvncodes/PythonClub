from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('getevents/', views.getevents, name='getevents'),
    path('eventdetail/<int:id>', views.eventdetail, name='details'),
    path('newevent/', views.newevent, name='newevent'),
]