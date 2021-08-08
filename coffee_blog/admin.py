from django.contrib import admin
from .models import Posts


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'is_published']
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', )


admin.site.register(Posts, PostsAdmin)
