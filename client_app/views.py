from .serializers import ItemSerializer
from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .forms import *

def index(request):
    form = LoginForm()
    message = 'username or password is incorrect'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username , password = password)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return redirect(reverse("items_api") + f'?token={token.key}')
            else:
                return render(request, 'login.html' , {'form':form, 'message': message})
        else:
                return render(request , 'login.html' , {'form':form , 'message': 'Enter Valid Data'})
    return render(request, 'login.html', {'form': form})


class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


