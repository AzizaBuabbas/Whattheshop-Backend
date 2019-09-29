from django.contrib.auth.models import User
from rest_framework import serializers
from .models import LanguageCourse , CartItem, Order

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password' , 'first_name' , 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username )
        new_user.set_password(password)
        new_user.save()
        return validated_data

class LanguageCourseListSerlializer(serializers.ModelSerializer):
    class Meta: 
        model = LanguageCourse
        fields = ['title' ,'price', 'id','logo','course_overview']

class LanguageCourseDetailSerlializer(serializers.ModelSerializer):
    class Meta: 
        model = LanguageCourse
        fields = ['title','price','course_overview','logo']
        
class ProfileSerializer(serializers.ModelSerializer):
    order_history = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["username", "order_history"]
    
    def get_order_history(self, obj ):
        orders = Order.objects.filter(user=obj)
        return OrderSeralizer(orders, many=True).data

class CartDetailSeralizer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["title", "cart", "quantity", "total"]

    def get_total(self, obj):
        return obj.quantity * obj.title.price


class OrderSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status"]


class CartItemSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["title", "quantity"]

class UpdateCartSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]


class ViewCartSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["cart"]

class CartSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["status", "title"]

    def get_item(self, obj):
        title = CartItem.objects.filter(cart=obj)
        return CartItemSeralizer(title, many=True).data

