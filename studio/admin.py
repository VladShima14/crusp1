from django.contrib import admin
from .models import Project, ProjectImage
# Register your models here.


class ProjectImageInLine(admin.TabularInline):
    model = ProjectImage


class AdminProject(admin.ModelAdmin):
    list_display = ['name', 'created']
    list_filter = ['name', 'created']

    inlines = [ProjectImageInLine]


admin.site.register(Project, AdminProject)
admin.site.register(ProjectImage)
