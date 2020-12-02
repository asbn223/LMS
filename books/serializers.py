from rest_framework import serializers
from core.models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'
        read_only_fields = ('id',)