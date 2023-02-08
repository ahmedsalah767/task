from odoo import models,fields,api



class DefaultSalesperson(models.Model):
    _inherit = 'res.partner'

    default_sp_customer= fields.Boolean(string="Default Salesperson Customer Info" , help="if selected it will set salesperson on saleorder from the field salesperson on the customer information")
    
    @api.onchange('default_sp_customer_info') 
    def set_salesperson(self): 
        company = self.env['res.company'].browse(self._context['company_id']) 
        if company.default_sp_customer and self.salesperson: 
            self._context['saleorder'].update({'salesperson': 'self.salesperson'}) 
        else:  
            self._context['saleorder'].update({'salesperson': 'self._uid'})