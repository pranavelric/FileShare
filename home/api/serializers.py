# from rest_framework import serializers
import shutil
from rest_framework import serializers
from ..models import Folder,File

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length=100000,allow_empty_file=False,use_url=False)
    )
    folder = serializers.CharField(required=False)

    def zip_files(self,folder):
        shutil.make_archive(f'static/{folder}','zip',f'static/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = File.objects.create(folder=folder,file= file)
            files_objs.append(files_obj)
        self.zip_files(folder.uid)
        return {'files':{},'folder':str(folder.uid)}