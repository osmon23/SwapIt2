from django.urls import path
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, UserLoginView, UserRegistrationView, RatingViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]

urlpatterns += router.urls
