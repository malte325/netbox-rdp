from django.shortcuts import render
from dcim.models import Device

def rdp_link(request, device_id):
    device = Device.objects.get(id=device_id)
    rdp_url = f"rdp://{device.primary_ip4.address}"
    return render(request, 'netbox_rdp/rdp_link.html', {'rdp_url': rdp_url})
