from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login', views.index, name='login'),
    path('items',views.ItemView.as_view(), name='items_api'),
    path('items/<int:pk>',views.SingleItemView.as_view()),
]