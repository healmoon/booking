from booking.api.views import UserModelViewSet
from booking.booking.urls import urlpatterns
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users',UserModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)