from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import LanguageCourse
from rest_framework.generics import ListAPIView , RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import LanguageCourse, CartItem, Order


class ItemView(ModelViewSet):
    queryset = LanguageCourse.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ItemSeralizer



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class LanguageCourseList(ListAPIView):
    queryset = LanguageCourse.objects.all()
    serializer_class = LanguageCourseListSerlializer

class LanguageCourseDetail(RetrieveAPIView):
    queryset = LanguageCourse.objects.all()
    serializer_class = LanguageCourseDetailSerlializer
    lookup_field = 'id'
    lookup_url_kwarg = 'course_id'

class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemSeralizer
    def perform_create(self, serializer):
        order, created = Order.objects.get_or_create(status="C", user=self.request.user)
        serializer.save(cart=order)

class ViewCartViewSet(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        order, created = Order.objects.get_or_create(status="C", user=user)
        return order


class FetchOrderViewSet(ListAPIView):
    queryset = Order.objects.exclude(status="C")
    serializer_class = OrderSeralizer


class ProfileViewSet(RetrieveAPIView):
    serializer_class = ProfileSerializer
    def get_object(self):
        return self.request.user

class UpdateCartViewSet(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = UpdateCartSeralizer
    lookup_field = "id"
    lookup_url_kwarg = "cart_id"
    
class CancelCartViewSet(DestroyAPIView):
    queryset = CartItem.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'

class Checkout(APIView):
    

    def get(self, request):
        cart = Order.objects.get(status="C", user=self.request.user)
        cart.status = "O"
        cart.save()
        return Response(CartSerializer(cart).data)
    