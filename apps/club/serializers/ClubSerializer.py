from rest_framework import serializers
from club.models import *
from rest_framework.validators import UniqueTogetherValidator

class ClubSerializer(serializers.ModelSerializer):
    club_administrator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = Club
        fields = '__all__'

    # validators = [
    #     UniqueValidator(
    #         queryset=Club.objects.all(),
    #         fields=('club_administrator', 'club'),
    #         message='已经创建过'
    #     )]

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('is_apply',)

class AttentionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = Attention
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Attention.objects.all(),
                fields=('user', 'club'),
                message='已经关注'
            )]


class AttentionListSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)


    username = serializers.SerializerMethodField(read_only=True)
    club_name = serializers.SerializerMethodField(read_only=True)

    def get_club_name(self,obj):
        if obj.club:
            return obj.club.club_name
        else:
            return None

    def get_username(self,obj):
        if obj.user:
            return obj.user.username
        else:
            return None

    class Meta:
        model = Attention
        fields = '__all__'

