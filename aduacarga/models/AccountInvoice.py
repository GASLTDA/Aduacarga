from odoo import fields, models, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    note_ids = fields.One2many('note','account_id')