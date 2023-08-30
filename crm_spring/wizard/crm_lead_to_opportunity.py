from odoo import models, _
from odoo.exceptions import ValidationError


class Lead2OpportunityPartner(models.TransientModel):
    _inherit='crm.lead2opportunity.partner'


    def action_apply(self):
        leads = self.env['crm.lead'].browse(self._context.get('active_ids', []))
        if any([lead.is_complete == False for lead in leads]):
            raise ValidationError(_("You can not convert opportunities due to not in complete stage.Please contact administrator."))
        return super(Lead2OpportunityPartner, self).action_apply()