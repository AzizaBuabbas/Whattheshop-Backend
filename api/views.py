from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import LanguageCourse
from rest_framework.generics import ListAPIView , RetrieveAPIView


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