from django.contrib import admin
from specialtiesDescriptions.models import *




class specAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Front,specAdmin)
admin.site.register(BackDecription,specAdmin)
admin.site.register(FullStackDecription,specAdmin)
admin.site.register(UiUxDecription,specAdmin)

