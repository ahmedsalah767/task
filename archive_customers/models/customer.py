from odoo import models,fields,api
from odoo.exceptions import UserError, AccessError, ValidationError


class Customer(models.Model):
    _inherit = 'res.partner'
    _description = "customer Details"

    def wiz(self):
        return {'type' : 'ir.actions.act_window',
                'res_model' : 'customer.archive',
                'view_mode' : 'form',
                'target' : 'new'}
    

    