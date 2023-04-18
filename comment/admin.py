from django.contrib import admin
from .models import Post, Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(active=True)
