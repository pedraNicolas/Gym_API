from django.urls import path
from api.views import ActivityView,ShiftView

urlpatterns = [
    path('activities/', ActivityView.as_view(), name='activities_list'),
    path('activities/<int:id>', ActivityView.as_view(), name='activities_process'),
    path('<str:activity_name>/shifts',ShiftView.as_view(),name='activity_shifts_list'),
    path('<str:activity_name>/shifts/<str:shift_name>',ShiftView.as_view(),name='activity_shifts_process'),
]
