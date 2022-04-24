from django.contrib import admin
from .models import File,Folder

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields =('folder','files')



@admin.register(Folder)
class FileAdmin(admin.ModelAdmin):
     readonly_fields=('uid','created_at')

