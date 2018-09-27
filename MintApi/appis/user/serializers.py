from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework import validators

User = get_user_model()
# Your Serializer

class UserRegisterSerializer(serializers.ModelSerializer):
    """
        用户
        序列类
    """
    username = serializers.CharField(required=True, allow_blank=False,
                                 validators=[validators.UniqueValidator(queryset=User.objects.all(), message='用户验证失败')],
                                 help_text='用户名', label='用户名')
    password = serializers.CharField(help_text='密码', label='密码', write_only=True,
                                     style={
                                         'input_type': 'password'
                                     })
    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        attrs['phone'] = attrs['username']
        print('attr =', attrs)
        # del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'password')