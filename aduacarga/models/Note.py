from odoo import models, fields, api

class Note(models.Model):
    _name='note'

    descripcion = fields.Many2one('expense.items',string='Descripción del gasto')
    cantidad = fields.Float('Cantidad')
    precio = fields.Monetary('Precio')
    valor = fields.Monetary('Valor')
    account_id = fields.Many2one('account.invoice')
    currency_id = fields.Many2one('res.currency', related='account_id.currency_id')


class ExpenseItems(models.Model):
    _name = 'expense.items'

    name = fields.Text(string='Nombre del gasto', required=True)