from rest_framework import serializers
from club.models import *

class TrainSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    train_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Train
        fields = '__all__'

class TrainUpdateSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    train_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Train
        fields = '__all__'
        read_only_fields = ('club',)
