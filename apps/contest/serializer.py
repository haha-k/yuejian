from rest_framework import serializers
from .models import *

class ContestSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    contest_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Contest
        fields = '__all__'