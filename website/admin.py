from django.contrib import admin
from website.models import contact , newsletter
# Register your models here.


class contactadmin(admin.ModelAdmin):
    date_hierarchy = ('created_at')
    list_display = ('name', 'email' , 'subject' , 'created_at')
    list_filter = ('email',)
    search_fields = ['name', 'massage']

admin.site.register(contact,contactadmin)
admin.site.register(newsletter)