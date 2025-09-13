from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'image',)
    search_fields = ('text', 'author__username', 'group__title')
    list_filter = ('pub_date', 'author', 'group',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description',)
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'post', 'created',)
    search_fields = ('text', 'author__username', 'post__text')
    list_filter = ('created', 'author', 'post',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following',)
    search_fields = ('user__username', 'following__username',)
    list_filter = ('user', 'following',)
    empty_value_display = '-пусто-'
