from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'published_date']
    list_display_links = ['title']

