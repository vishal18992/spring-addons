from odoo import models, fields, api, _, SUPERUSER_ID


class CrmLead(models.Model):
    _inherit = "crm.lead"

    provinces = fields.Many2many("res.country.state", string="Provinces")
    opportunity_type = fields.Selection([('technology', _('Technology')), \
        ('business', _('Business'))], string="Opportunity Type")
    opportunity_type_name = fields.Char(string="Opportunity Type Name")
    is_complete = fields.Boolean(string="IsComplete", \
        compute='_compute_is_complete')


    @api.depends('stage_id')
    def _compute_is_complete(self):
        flag = False 
        for lead in self:
            if lead.stage_id.is_complete == True:
                flag = True
            lead.is_complete = flag

    @api.model
    def default_get(self, default_fields):
        res = super().default_get(default_fields)
        context = self.env.context
        if context.get('default_type') == 'lead':
            stage_id = self.env['crm.stage'].search([('type', '=', 'lead'),\
                 ('is_won', '=', False)], limit=1, order="sequence")
            res.update({'stage_id': stage_id.id})
        return res


    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stages = super(CrmLead, self)._read_group_stage_ids(stages=stages,\
             domain=domain, order=order)
        return stages.filtered(lambda s: s.type == self.type)

    
    def _stage_find(self, team_id=False, domain=None, order='sequence, id', limit=1):
        stages = super(CrmLead, self)._stage_find(team_id=team_id, \
            domain=domain, order=order, limit=limit)
        return stages.filtered(lambda s: s.type == self.type)

    def action_complete(self):
        leads_by_complete_stage = {}
        for lead in self:
            complete_stages = self._stage_find(domain=[('is_won', '=', True)],\
                 limit=None)
            stage_id = next((stage for stage in complete_stages \
                if stage.sequence > lead.stage_id.sequence), None)
            if not stage_id:
                stage_id = next((stage for stage in reversed(complete_stages) \
                    if stage.sequence <= lead.stage_id.sequence), complete_stages)
            if stage_id in leads_by_complete_stage:
                leads_by_complete_stage[stage_id] += lead
            else:
                leads_by_complete_stage[stage_id] = lead
        for complete_stage_id, leads in leads_by_complete_stage.items():
            leads.write({'stage_id': complete_stage_id.id, 'probability': 100})
        return True


    def convert_opportunity(self, partner, user_ids=False, team_id=False):
        customer = partner if partner else self.env['res.partner']
        for lead in self:
            if not lead.active or lead.probability == 100:
                continue
            lead.type= "opportunity"
            lead.stage_id = False
            vals = lead._convert_opportunity_data(customer, team_id)
            vals.update({'opportunity_type': "technology"})
            lead.write(vals)

            new_opportunity = lead.copy({'opportunity_type': "business"})
            opportunity_vals = new_opportunity._convert_opportunity_data(customer, team_id)
            new_opportunity.write(opportunity_vals)

        if user_ids or team_id:
            self._handle_salesmen_assignment(user_ids=user_ids, team_id=team_id)

        return True