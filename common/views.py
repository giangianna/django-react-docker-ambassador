from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        return Response('hello')
