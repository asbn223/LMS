from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from core.models import Books


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            msg = _("Invalid Credentials, Please try again")
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'
        read_only_fields = ('id',)