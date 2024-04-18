from rest_framework import serializers
from Aether.models import *
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(),
                                              required=False)  # ������ ���� user ��������������

    class Meta:
        model = Address
        fields = '__all__'