from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.settings import api_settings
from account.models import Account
from rest_framework.validators import UniqueValidator
from datetime import datetime



class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    class Meta:
        model = Account
        # fields = '__all__'
        fields = ("id","token","username","password","telephone","email")
        extra_kwargs={
            'username': {
                'min_length': 2,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许2-20个字符的用户名',
                    'max_length': '仅允许2-20个字符的用户名',
                },
                "validators":[UniqueValidator(queryset =Account.object.all())]
            },
            'password': {
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            },
        }


    def create(self,validated_data):
        user = Account.object.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['telephone'],
            validated_data['password'],
        )

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        user.token = token

        return user



class updatePassword(ModelSerializer):
    pass


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    last_login = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    def get_days_since_joined(self,obj):
        dt = obj.register_time.replace(tzinfo=None)
        return (datetime.now()-dt).days

    class Meta:
        model = Account
        exclude = ("first_name","last_name","date_joined","register_time")
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            },
        }

    # def update(self,instance,validated_data):
    #     password = validated_data.get('password',instance.password)
    #     print("uuuuuup"+password)
    #     print(validated_data)
    #     instance.set_password(password)
    #     instance.save()
    #     return instance

