from django.contrib import admin
from .models import Technology, Screenshot, Category, Project
import os


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority_order']
    list_filter = ['categories']
    ordering = ['priority_order']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority_order']
    prepopulated_fields = {'name': ('title',)}
    ordering = ['priority_order']

class ScreenshotAdmin(admin.ModelAdmin):
    list_display= ['project', 'priority_order']
    ordering = ['project', 'priority_order']

admin.site.register(Technology)
admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.site_url = (
    'http://localhost:3000/'
    if (os.environ.get('DEBUG_VALUE') == 'True')
    else 'https://gbertl.vercel.app/'
)
