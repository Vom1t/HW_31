

from django.urls import path

from selection import views


urlpatterns = [
   path('', views.SelectionListView.as_view(), name='selections'),
   path("<int:pk>/update/", views.SelectionUpdateView.as_view(), name="update_selection"),
   path("<int:pk>/delete/", views.SelectionDeleteView.as_view(), name="delete_selection"),
   path('<int:pk>/', views.SelectionDetailView.as_view(), name='detail_selection'),
   path('create/', views.SelectionCreateView.as_view(), name='create_selection'),
]