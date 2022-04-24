import os
from django.db import models
import uuid

def get_upload_path(instance,filename,*args,**kwargs):
    return os.path.join(str(instance.folder.uid),filename)

class Folder(models.Model):
    uid =  models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)


class File(models.Model):
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
