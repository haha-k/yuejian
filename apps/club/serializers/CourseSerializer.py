from rest_framework import serializers
from club.models import *

class CourseSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class CourseUpdateSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = Course
        # exclude = ('club',)
        fields = '__all__'
        read_only_fields = ('club',)
        # extra_fields = {
        #     'club':{
        #         'read_only':True,
        #     }
        # }