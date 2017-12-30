from django.contrib import admin
from .models import Profile, Post, Comment, ExternalProfile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instnaces(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instnaces(request, obj)

class PostAdmin(admin.ModelAdmin):
    list_display = ['reservation_date', 'author', 'title', ]
    list_display_links = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message']
    list_display_links = ['message']

class ExternalProfileAdmin(admin.ModelAdmin):
    list_display = ['author', 'link', 'introduction', ]
    list_display_links = ['author']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ExternalProfile, ExternalProfileAdmin)