from django.contrib import admin
from contact.models import *



class contactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Adresse,contactAdmin)
admin.site.register(Phone,contactAdmin)
admin.site.register(Email,contactAdmin)
