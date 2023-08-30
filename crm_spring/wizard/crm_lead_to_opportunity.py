from odoo import models, _
from odoo.exceptions import ValidationError


class Lead2OpportunityPartner(models.TransientModel):
    _inherit='crm.lead2opportunity.partner'


    def _action_convert(self):
        result_opportunities = self.env['crm.lead'].browse(self._context.get('active_ids', []))
        opportunity_type_leads = self.env['crm.lead']
        for lead in result_opportunities:
            lead.opportunity_type = 'technology'
            new_opportunity = lead.copy({'opportunity_type': "business"})
            opportunity_type_leads |= new_opportunity
        result_opportunities |= opportunity_type_leads
        context = self.env.context.copy()
        context.update({'active_ids': result_opportunities.ids})
        self.env.context = context
        return super(Lead2OpportunityPartner, self)._action_convert()

    def action_apply(self):
        leads = self.env['crm.lead'].browse(self._context.get('active_ids', []))
        if not any([lead.is_complete == False for lead in leads]):
            raise ValidationError(_("You can not convert opportunities due to not in complete stage.Please contact administrator."))
        return super(Lead2OpportunityPartner, self).action_apply()