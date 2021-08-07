from django.contrib import admin
from .models import Posts
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст", widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'is_published']
    list_display_links = ('id', 'title')
    form = PostAdminForm
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', )


admin.site.register(Posts, PostsAdmin)
