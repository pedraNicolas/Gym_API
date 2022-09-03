from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Activity, Shift
from .serializers import ActivitySerializer
import json

# Create your views here.


class ActivityView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            activities = list(Activity.objects.filter(activity_id=id).values())
            if len(activities) > 0:
                activity = activities[0]
                data = {'message': "Success", 'activity': activity}
            else:
                data = {'message': "Activity not found ..."}
            return JsonResponse(data)
        else:
            activities = list(Activity.objects.values())
            if len(activities) > 0:
                data = {'message': "Success", 'activities': activities}
            else:
                data = {'message': "Activities not found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Activity.objects.create(activity_name=jd['activity_name'].lower(), start_time=jd['start_time'],
                                finish_time=jd['finish_time'], shift_duration=jd['shift_duration'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        activities = list(Activity.objects.filter(activity_id=id).values())
        if len(activities) > 0:
            activity = Activity.objects.get(activity_id=id)
            activity.activity_name = jd['activity_name'].lower()
            activity.start_time = jd['start_time']
            activity.finish_time = jd['finish_time']
            activity.shift_duration = jd['shift_duration']
            activity.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Activity not found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        activities = list(Activity.objects.filter(activity_id=id).values())
        if len(activities) > 0:
            Activity.objects.filter(activity_id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Activity not found ..."}
        return JsonResponse(data)


class ShiftView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, activity_name):
        activities = list(Activity.objects.filter(
            activity_name=activity_name).values())
        if len(activities) > 0:
            activity_id = activities[0]['activity_id']
            shifts = list(Shift.objects.filter(
                activity_id=activity_id).values())
            data = {'message': "Success", 'shifts': shifts}
        else:
            data = {'message': "Shift not found ..."}
        return JsonResponse(data)

    def delete(self, request, activity_name, shift_name):
        activities = list(Activity.objects.filter(
            activity_name=activity_name).values())
        print(activities)
        if len(activities) > 0:
            activity_id = activities[0]['activity_id']
            shifts = list(Shift.objects.filter(
                shift_name=shift_name).filter(activity_id=activity_id).values())
            if len(shifts) > 0:
                Shift.objects.filter(shift_name=shift_name).filter(
                    activity_id=activity_id).delete()
                data = {'message': "Success"}
            else:
                data = {'message': "Shift not found ..."}
        else:
            data = {'message': "Activity not found ..."}
        return JsonResponse(data)

