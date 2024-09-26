from django.db import models

class RDPConnection(models.Model):
    device = models.ForeignKey('dcim.Device', on_delete=models.CASCADE)
    rdp_url = models.URLField()

    def __str__(self):
        return self.rdp_url
