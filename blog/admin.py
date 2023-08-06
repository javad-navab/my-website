from django.contrib import admin
from blog.models import post
# Register your models here.
# @admin.register(post)
class PostAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views' , 'status', 'published_at', 'created_at' )
    list_filter =('status',)
    # ordering = ('created_at',)
    search_fields = ('title','content')
admin.site.register(post , PostAdmin)