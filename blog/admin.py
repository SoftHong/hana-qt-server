from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['reservation_date', 'author', 'title', 'external_author', ]
    list_display_links = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message']
    list_display_links = ['message']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)