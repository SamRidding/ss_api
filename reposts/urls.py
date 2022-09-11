from django.urls import path
from reposts import views

urlpatterns = [
    path('reposts/', views.RepostList.as_view()),
    path('reposts/<int:pk>/', views.RepostDetail.as_view())
]
