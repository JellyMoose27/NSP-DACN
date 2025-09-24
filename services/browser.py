import threading
import socket
import time
from zeroconf import *

class OdooListener(object):
    def __init__(self):
        self.r = Zeroconf()
    
    def add_service(self, zeroconf, type, name):
        info = self.r.get_service_info(type, name)
        if info:
            ip = info.parsed_addresses()[0] if info.parsed_addresses() else None
            self.env['zeroconf.service'].create({
                "name": name,
                "ip_address": ip,
                "port": info.port,
                "properties": str(info.properties)
            })

    def remove_service(self, zeroconf, type, name):
        record = self.env['zeroconf.service'].search([("name", "=", name)], limit=1)
        if record:
            record.unlink()
        else:
            pass
        
def start_browser(env):
    zeroconf = Zeroconf()
    listener = OdooListener(env)
    ServiceBrowser(zeroconf, "_odoo._tcp.local", listener)