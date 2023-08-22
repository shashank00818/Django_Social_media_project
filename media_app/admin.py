from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','user','caption','image','created_at','updated_at']

# admin.site.register(Post)