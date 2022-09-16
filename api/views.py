from django.shortcuts import render

from django.views.generic import UpdateView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from author.models import Author
from .serializers import AuthorSerializer


# class VIEWS FOR AUTHOR API

class AuthorListCreateView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()
    permission_classes = (IsAdminUser,)


class AuthorListDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()
    permission_classes = (AllowAny,)


class AuthorAPIDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()
    permission_classes = (IsAdminUser,)
    messages = 'success deleted'


