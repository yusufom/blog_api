from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Tag, Category

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "read_time"]
    list_filter = ["updated", "timestamp"]
    prepopulated_fields =   {'slug': ('title',)}
    
    search_fields = ["title", "content"]
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
