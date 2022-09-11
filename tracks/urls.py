from django.urls import path
from tracks import views

urlpatterns = [
    path('tracks/', views.TrackList.as_view()),
    path('tracks/<int:pk>/', views.TrackDetail.as_view())
]
