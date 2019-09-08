from rest_framework import serializers
from .models import Activity,Apply
from club.models import Train
from activity.models import *
from account.models import *
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

    train_title = serializers.SerializerMethodField(read_only=True)
    activity_title = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    def get_train_title(self,obj):
        if obj.train:
            return obj.train.train_title
        else:
            return None

    def get_activity_title(self,obj):
        if obj.activity:
            return obj.activity.activity_title
        else:
            return None

    def get_username(self,obj):
        if obj.user:
            return obj.user.username
        else:
            return None

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
