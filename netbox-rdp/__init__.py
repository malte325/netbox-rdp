from extras.plugins import PluginConfig

class NetboxRDPConfig(PluginConfig):
    name = 'netbox_rdp'
    verbose_name = 'Netbox RDP'
    description = 'Ein Plugin, um RDP-Verbindungen direkt aus der Geräteübersicht zu starten.'
    version = '1.0'

config = NetboxRDPConfig
