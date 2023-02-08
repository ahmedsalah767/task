from odoo import models,fields,api


class Wizard(models.TransientModel):
    _name = 'customer.archive'
    _description = 'archive inactive customers'

    def customer_archive(self):
        for customer in self: 
            sale_orders = self.env['sale.order_count'] 
        invoicing_amount = 0  
        for invoice in self.env['total_invoiced']:
            invoicing_amount = invoice
        due_amount = 0    
        for payment in self.env['debit']:  
            due_amount = debit  
        if not sale_orders and invoicing_amount == 0 and due_amount == 0 and not picking_warn and not purchase_warn:  
            customer._set({'active': False})
        return True