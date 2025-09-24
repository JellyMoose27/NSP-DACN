from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class VehicleLogs(models.Model):
    _name        =  'nsp.vehicle.logs'
    _description =  'Lịch sử ra vào của phương tiện'
    _order       =  'create_date desc'
    _rec_name    =  'display_name'
    
    vehicle_id =    fields.Many2one('nsp.vehicle', string="Phương tiện", required=True, ondelete='cascade')
    partner_id =    fields.Many2one('res.partner', string="Người sở hữu", required=True, ondelete='cascade')

    display_name =  fields.Char(string="Tên hiễn thị", compute='_compute_display_name', store=True)
    partner_name =  fields.Char(string="Tên người sở hữu", related='partner_id.name', store=True)
    vehicle_name =  fields.Char(string="Tên phương tiện", related='vehicle_id.name', store=True)
    plate_number =  fields.Char(string="Biển số xe", related="vehicle_id.plate_number", store=True)

    direction =     fields.Selection([
                    ('in', 'vào'),
                    ('out', 'ra')
                    ], string='Hướng', required=True)

    #SQL constrains
    _sql_constrains = [
        ('check_direction', "CHECK (direction IN ('in','out'))", "Hướng phải là 'in' hoặc 'out'"),
    ]

    @api.depends('vehicle_id', 'direction', 'create_date')
    def _compute_display_name(self):
        """Tính tên hiễn thị cho log"""
        for record in self:
            if record.vehicle_id and record.direction and record.create_date:
                direction_text = 'vào' if record.direction == 'in' else 'ra'
                record.display_name = _(f"{record.vehicle_id.plate_number} - {direction_text} ({record.create_date.strftime('%d/%m/%Y %H:%M:%S')})")
            else:
                record.display_name = _("Log chưa đầy đủ thông tin")