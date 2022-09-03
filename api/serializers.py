from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'activity_id',
            'activity_name',
            'start_time',
            'finish_time',
            'shift_duration',
            'activity_on_monday',
            'activity_on_tuesday',
            'activity_on_wednesday',
            'activity_on_thursday',
            'activity_on_friday',
            'activity_on_saturday',
        )

