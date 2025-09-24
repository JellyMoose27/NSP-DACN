from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class Device(models.Model):
    """Các thiết bị đã được khám phá"""
    _name        = "nsp.devices"
    _description = "Thiết bị được khám phá trong mạng local"

    name         = fields.Char(string="Tên thiết bị")
    ip           = fields.Char(string="Địa chỉ IP")
    services     = fields.Char(string="Dịch vụ thiết bị")
    port         = fields.Integer(string="Port")