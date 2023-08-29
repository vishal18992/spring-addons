from odoo import models, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"

    provinces = fields.Many2many("res.country.state", string="Provinces")
    opportunity_type = fields.Selection([('technology', 'Technology'), ('business', 'Business')], string="Opportunity Type")
    opportunity_type_name = fields.Char(string="Opportunity Type Name")