from django.contrib import admin
from .models import Project

# Register your models here.

admin.site.site_header = "Panel de administración de SOB24H"


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
