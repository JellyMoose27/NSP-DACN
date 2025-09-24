from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class Role(models.Model):
    _name        =  'nsp.role'
    _description =  'Quyền truy cập cho người dùng'

    name      = fields.Char(string="Tên quyền", required=True)
    group_ids = fields.Many2many(
        'res.groups',
        string="Các quyền truy cập",
    )
