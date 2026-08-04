from django.contrib import admin
from . import models

class CommentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','text','created_at')
admin.site.register(models.Comment,CommentAdmin)
