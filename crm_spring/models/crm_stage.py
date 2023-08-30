from odoo import models, fields


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    type = fields.Selection([('lead', 'Lead'), ('opportunity', 'Opportunity')], index=True, default="opportunity")
    is_complete = fields.Boolean(string="Is Complete Stage", default=False)