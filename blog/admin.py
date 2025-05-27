from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('title', 'body', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
