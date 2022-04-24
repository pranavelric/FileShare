import json
from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework_json_api.views import ModelViewSet
from rest_framework.response import Response
from .api.serializers import *
from rest_framework import status


def home(request):
    return render(request,'home/home.html')

def download(request,uid):
    return render(request,'home/download.html',context={"uid":uid})

class HandleFileUpload(ModelViewSet):
    serializer_class = FileListSerializer
    queryset = File.objects.all()


    def create(self,request):
        try:
            data=  request.data
            serializer = FileListSerializer(data= data)

            if serializer.is_valid():
                file_obj = serializer.save()
                return Response(file_obj,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(json.dumps({'error': f'{e}'}))