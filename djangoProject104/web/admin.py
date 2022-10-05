from django.contrib import admin
from djangoProject104.web.models import Employees


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    pass
