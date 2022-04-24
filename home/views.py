import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .api.serializers import *
from rest_framework import status

class HandleFileUpload(APIView):

    def post(self,request):
        try:
            data=  request.data
            serializer = FileListSerializer(data= data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(json.dumps({'error': f'{e}'}))