from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('', views.index),
    path('items',views.ItemView.as_view()),
    path('items/<int:pk>',views.SingleItemView.as_view()),
    path('auth-token',obtain_auth_token)
]