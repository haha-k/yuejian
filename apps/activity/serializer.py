from rest_framework import serializers
from .models import Activity,Apply
from rest_framework.validators import UniqueTogetherValidator

class ActivitySerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    activity_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Activity
        fields = '__all__'

class ApplySerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)


    class Meta:
        model = Apply
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Apply.objects.all(),
                fields=('user', 'activity'),
                message='已经报名活动'
            ),
            UniqueTogetherValidator(
                queryset=Apply.objects.all(),
                fields=('user', 'train'),
                message='已经报名训练'
            )]
