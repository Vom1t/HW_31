from django.urls import path

from ads.views.category import *


urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>', CatDetailView.as_view())
]
