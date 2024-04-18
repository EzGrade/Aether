from rest_framework import serializers
from Aether.models import *
from productapp.serializers import ProductSerializer
from orderapp.models import (Address,
                             Order,
                             OrderDetails,
                             OrderStatus,
                             Payment
                             )
from accountapp.serializers import AccountSerializer
from addressapp.serializers import AddressSerializer


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='address.address', read_only=True)

    class Meta:
        model = OrderDetails
        fields = '__all__'


class OrderDetailsNewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)
    product_write_only = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True,
                                                            required=False, source='product')  # ������������� ����
    address_s = serializers.CharField(source='address.address', read_only=True)
    product_s = serializers.CharField(source='product.name', read_only=True)
    product_detail = ProductSerializer(source='product', read_only=True)  # �������� ��� ���� ��� ProductSerializer

    class Meta:
        model = OrderDetails
        fields = '__all__'


class OrderDetailsFCSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)

    class Meta:
        model = OrderDetails
        fields = '__all__'


class OrderDetailsAloneSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(),
                                              required=False)  # ������ ���� user ��������������

    # product_s = serializers.CharField(source='product.name', read_only=True)
    # address_s = serializers.CharField(source='address.address', read_only=True)

    class Meta:
        model = OrderDetails
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer()
    order_details = OrderDetailsNewSerializer()  # ������ many=True �����

    class Meta:
        model = Order
        fields = '__all__'


class OrderNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ('quantity',)


class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)
    order = OrderDetailsSerializer()
    account = AccountSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
