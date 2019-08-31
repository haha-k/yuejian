from rest_framework import serializers
from .models import *


class PictureSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    def __str__(self):
        return self.url

    class Meta:
        model = Picture
        # fields = ("user","url")
        fields = ("picture_id","url","user", "create_time", "update_date")

class PictureDetailSerializer(PictureSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Picture
        fields = ("picture_id","url","user", "create_time", "update_date")




# class PictureUpdateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault(),)

#     # pics=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=True,write_only=True)

#     class Meta:
#         model = Picture
#         fields = ("url","user")





class PictureListSerializer(serializers.ModelSerializer):

    pics = serializers.ListField(
        child=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=True),
        write_only=True)

    photo = serializers.ListField(
        child = serializers.CharField(max_length=1000,),
        read_only = True
    )

    class Meta:
        model = Picture
        fields = ("photo","pics","create_time",)

    def create(self,validated_data):
        pic = validated_data['pics']
        print(pic)
        images = []
        user_id = 1
        for index,url in enumerate(pic):
            image = Picture.objects.create(url=url,user=Account.objects.get(id=self.context['request'].user.id))
            pics = PictureSerializer(image,context=self.context)
            print(pics.data)
            # user_id = pics.data['user']
            images.append(pics.data['url'])
        print(user_id)
        return {
            "photo":images,
        }


class BlueprintSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = Blueprint
        fields = '__all__'

