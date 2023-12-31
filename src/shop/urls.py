from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("toys/", views.ToyList.as_view()),
    path("toys/<int:pk>/", views.ToyDetail.as_view()),
    path("orders/", views.OrderList.as_view()),
    path("orders/<int:pk>/", views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
