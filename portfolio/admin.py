from django.contrib import admin
from .models import Role, Technology, Screenshot, Category, Project, ProjectScreenshot

class ProjectScreenshotAdmin(admin.ModelAdmin):
    list_filter = ['project']

    def get_ordering(self, request):
        return ['priority_order']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority_order']

    def get_ordering(self, request):
        return ['priority_order']

admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(Screenshot)
admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectScreenshot, ProjectScreenshotAdmin)
