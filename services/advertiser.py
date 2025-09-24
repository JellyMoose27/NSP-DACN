from zeroconf import *
import socket

class OdooAdvertiser:
    def __init__(self, port=8069, service_name="Odoo Instance"):
        self.zeroconf = Zeroconf()
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        self.info = ServiceInfo(
            type_ = "_odoo._tcp.local.",
            name=f"{service_name}._odoo._tcp.local.",
            port=port,
            addresses=[socket.inet_aton(local_ip)],
            properties={"version": "18.0"},
            server=f"{hostname}.local."
        )
    
    def register(self):
        self.zeroconf.register_service(self.info)
    
    def unregister(self):
        self.zeroconf.unregister_service(self.info)
        self.zeroconf.close()