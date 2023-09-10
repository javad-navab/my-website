from django.contrib import admin
from blog.models import post,category,comment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# @admin.register(post)
class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'id' , 'author' , 'counted_views' , 'status', 'published_at', 'created_at' )
    list_filter =('status', 'author')
    # ordering = ('created_at',)
    search_fields = ('title','content')
    summernote_fields = ('content',)


class commentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('name', 'id' , 'post' , 'approved' , 'created_at' , 'updated_at' )
    list_filter =('post', 'approved')
    search_fields = ('name','post')


admin.site.register(comment,commentAdmin)
admin.site.register(category)
admin.site.register(post , PostAdmin)