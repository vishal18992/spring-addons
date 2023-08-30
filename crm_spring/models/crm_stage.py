from odoo import models, fields


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    type = fields.Selection([('lead', 'Lead'), ('opportunity', 'Opportunity')], index=True, default="opportunity")