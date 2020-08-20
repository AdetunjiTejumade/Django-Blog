from django.contrib import admin

from .models import Blog
from .models import Comment
# Register your models here.

#can change into tabularInline "admin.TabularInline"
# "admin.StackedInline" shows comments in a stacked format
class CommentInline(admin.TabularInline): 
    model = Comment
    extra = 0 # removes all extra empty fields


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
