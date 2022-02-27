from math import fabs
from django.contrib import admin

# Register your models here.
from homeDescription.models import Description

class descriptionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Description, descriptionAdmin)
