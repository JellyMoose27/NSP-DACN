from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Vehicle(models.Model):
    _name        =  'nsp.vehicle'
    _description =  "Phương tiện của người dùng"
    _rec_name    =  'plate_number'

    name         =   fields.Char(string='Tên phương tiện', required=True)
    brand        =   fields.Char(string="Hãng xe")
    plate_number =   fields.Char(string="Biển số xe", size=20, required=True)
    color        =   fields.Char(string="Màu xe")

    #Tracking trạng thái xe
    last_direction = fields.Selection([
        ('in', 'vào'),
        ('out', 'ra'),
        ], string="Hướng cuối cùng", default='in')
    
    current_status = fields.Selection([
        ('inside', 'Trong bãi'),
        ('outside', 'Ngoài bãi'),
        ('unknown', "Không xác định")
        ], string="Trạng thái hiện tại", default='unknown', store=True)

    owner_partner_id = fields.Many2one('res.partner', string="Chũ sở hữu")

    #SQL constrains
    _sql_constrains = [
        ('plate_number_unique', 'UNIQUE(plate_number)', 'Biển số xe phải là duy nhất'),
    ]

    @api.depends('last_direction')
    def _compute_current_status(self):
        """Tính trạng thái hiện tại dựa vào hướng cuối cùng"""
        for vehicle in self:
            if vehicle.last_direction == 'in':
                vehicle.current_status = 'inside'
            elif vehicle.last_direction == 'out':
                vehicle.current_status = 'outside'
            else:
                vehicle.current_status = 'unknown'
            
    @api.model
    def create(self, vals):
        """Overwrite phương thức tạo"""
        vehicle = super().create(vals)
        return vehicle
    
    def write(self, vals):
        """Overwrite phương thức chỉnh"""
        res = super().write(vals)
        return res