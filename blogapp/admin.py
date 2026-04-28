from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'get_word_count')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'content', 'image')
        }),
        ('Author', {
            'fields': ('author',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
        }),
    )
    
    def get_word_count(self, obj):
        return len(obj.content.split())
    get_word_count.short_description = 'Word Count'
