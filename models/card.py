from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Card(models.Model):
    """Thẻ nhân viên cho NSP"""
    _name           = 'nsp.card'
    _description    = 'Thẻ nhân viên để cấp cho nhân viên sử dụng hệ thống NSP'
    _inherit        = ['mail.thread','mail.activity.mixin']

    card_id     = fields.Char(string="ID", required=True)
    card_type   = fields.Selection([
        ('student', "Sinh viên"),
        ('staff', "Nhân viên")
        ], string="Loại thẻ", default="student")
    
    owner_name = fields.Char(string="Tên sở hửu", required=True)
    partner_id = fields.Many2one(
        "res.partner",
        string="Người sở hữu",
        required=True,
        ondelete="cascade"
    )

    _sql_constraints = [
        ('unique_partner_card', 'unique(partner_id)', 'Mỗi người chỉ được cấp một thẻ!')
    ]

    