from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, CompanyViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'company', CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]