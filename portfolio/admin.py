from django.contrib import admin
from .models import Role, Technology, Screenshot, Category, Project, ProjectScreenshot
import os

class ProjectScreenshotAdmin(admin.ModelAdmin):
    list_filter = ['project']

    def get_ordering(self, request):
        return ['priority_order']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority_order']
    list_filter = ['categories']

    def get_ordering(self, request):
        return ['priority_order']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('title',)}

admin.site.site_url = 'http://localhost:3000/' if (os.environ.get('DEBUG_VALUE') == 'True') else 'https://gilbertlc.com/'

admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(Screenshot)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectScreenshot, ProjectScreenshotAdmin)
