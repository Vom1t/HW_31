from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import *

from django.urls import path



urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='get_user_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_user_token'),

]