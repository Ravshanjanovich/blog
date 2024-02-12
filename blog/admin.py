from django.contrib import admin
from blog.models import Post, Comment



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'slug', 'author','publish','status')
    list_filter = ('title','slug','author')
    search_fields = ('slug', 'title')
    ordering = ("status",'publish')
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'post','created', 'active')
    list_filter = ('active', 'created', 'active')
    search_fields = ('name', 'email', 'body')


