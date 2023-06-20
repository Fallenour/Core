from django.urls import path
from .views import EventList, EventDetail, SystemList, SystemDetail

urlpatterns = [

    path('event/', EventList.as_view()),
    path('event/<int:pk>/', EventDetail.as_view()),
    path('system/', SystemList.as_view()),
    path('system/<int:pk>/', SystemDetail.as_view()),

]