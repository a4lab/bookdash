from django.contrib import admin

from images.models import Image

# Register your models here.
@admin.register(Image)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'body', 'image', 'created']
#     list_filter = ['created']
                                                    