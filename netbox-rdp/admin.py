from django.contrib import admin
from .models import RDPConnection

@admin.register(RDPConnection)
class RDPConnectionAdmin(admin.ModelAdmin):
    list_display = ('device', 'rdp_url')
