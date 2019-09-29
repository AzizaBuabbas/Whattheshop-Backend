from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from api import views 

router = SimpleRouter()
router.register("LanguageCourse", views.ItemView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('list/', views.LanguageCourseList.as_view(), name="languagecourse-list"),
    path('detail/<int:course_id>/', views.LanguageCourseDetail.as_view(), name='languagecourse-detail'),
    path('', include(router.urls)),
    path('profile/', views.ProfileViewSet.as_view()),
    path('order/', views.FetchOrderViewSet.as_view()),
    path('addtocart/', views.CartItemCreateAPIView.as_view()),
    path('viewcart/', views.ViewCartViewSet.as_view()),
    path('updatecart/<int:cart_id>/', views.UpdateCartViewSet.as_view()),
    path('deletecart/<int:cart_id>/', views.CancelCartViewSet.as_view()),
    path('checkout/', views.Checkout.as_view()),
]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)