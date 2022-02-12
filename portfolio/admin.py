from django.contrib import admin
from .models import Role, Technology, Screenshot, Category, Project
import os


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority_order']
    list_filter = ['categories']

    def get_ordering(self, request):
        return ['priority_order']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority_order']
    prepopulated_fields = {'name': ('title',)}

    def get_ordering(self, request):
        return ['priority_order']


admin.site.site_url = (
    'http://localhost:3000/'
    if (os.environ.get('DEBUG_VALUE') == 'True')
    else 'https://gilbertlc.com/'
)

admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(Screenshot)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
