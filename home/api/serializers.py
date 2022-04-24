from rest_framework_json_api import serializers
import shutil
from ..models import Folder,File
from collections import *
from rest_framework.fields import  SkipField
from rest_framework.relations import  PKOnlyObject

from django.conf import settings


class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length=100000,allow_empty_file=False,use_url=False)
    )
    folder = serializers.CharField(required=False)


    def zip_files(self,folder):
        shutil.make_archive(f'static/zip/{folder}','zip',f'static/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = File.objects.create(folder=folder,files= file)
            files_objs.append(files_obj)
        self.zip_files(folder.uid)
        return {'files':{},'folder':str(folder.uid)}
    
    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self._readable_fields
        if isinstance(instance, bytes):
                instance = instance.decode("utf-8")

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            else:
                ret[field.field_name] =str(attribute)

        return ret

    class Meta:
        resource_name="file"
