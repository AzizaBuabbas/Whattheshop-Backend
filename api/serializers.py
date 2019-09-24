from django.contrib.auth.models import User
from rest_framework import serializers
from .models import LanguageCourse

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password' , 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        Email   =  validated_data['email']
        new_user = User(username=username , email=Email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class LanguageCourseListSerlializer(serializers.ModelSerializer):
    class Meta: 
        model = LanguageCourse
        fields = ['title' ,'price', 'id','logo']

class LanguageCourseDetailSerlializer(serializers.ModelSerializer):
    class Meta: 
        model = LanguageCourse
        fields = ['title','price','course_overview','logo']


