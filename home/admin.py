from django.contrib import admin
from .models import File,Folder

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields =('folder','file')



@admin.register(Folder)
class FileAdmin(admin.ModelAdmin):
    fields =('uid','created_at')

