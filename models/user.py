from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit  = "res.partner"
    _rec_name = "name"

    citizen_id       =  fields.Char(string="CCCD/CMND", help="CCCD/CMND của người sở hữu")

    card_id          =  fields.One2many('nsp.card', 'partner_id',string="Thẻ nhân viên")
    vehicle_ids      =  fields.One2many('nsp.vehicle', 'owner_partner_id', string="Phương tiện sở hữu")
    partner_logs_ids =  fields.One2many('nsp.vehicle.logs', 'partner_id', string="Lịch sử ra vào")
    user_ids         =  fields.One2many('res.users', 'partner_id', string="Linked Users")

    #SQL Contrains
    _sql_constraints = [
        ('citizen_id_unique', 'unique(citizen_id)', 'CCCD/CMND phải là duy nhất')
    ]

    @api.constrains('citizen_id')
    def check_unique_citizen_id(self):
        """Kiểm tra CCCD/CMND là duy nhất hay không"""
        for record in self:
            if record.citizen_id:
                #Kiểm tra độ dài (CCCD: 12, CMND: 9)
                if len(record.citizen_id) not in [9,12]:
                    raise ValidationError(_("CCCD phải có 12 chữ số và CMND phải có 9 chữ số"))
                #Kiểm tra chữ số
                if not record.citizen_id.isdigit():
                    raise ValidationError(_("CCCD/CMND phải là số"))