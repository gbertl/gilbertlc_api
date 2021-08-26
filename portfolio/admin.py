from django.contrib import admin
from .models import Role, Technology, Screenshot, Category, Project, ProjectScreenshot

admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(Screenshot)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectScreenshot)
