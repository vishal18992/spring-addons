import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

CRM_FIELDS = ['name', 'phone', "user_id", "partner_id"]


class CrmLeadController(http.Controller):

    @http.route("/lead", type='json', auth="public", methods=['POST'], csrf=False)
    def crm_lead_create(self, **kwrgs):
        record = dict({})
        partner_obj = request.env['res.partner']
        lead = request.env['crm.lead']

        [ record.update({val: kwrgs.get(val, '')}) for val in CRM_FIELDS]
        
        customer = partner_obj.search([('name', '=', kwrgs.get('customer'))])
        sales_person = request.env['res.users'].search(['|', ('name', '=', kwrgs.get('salesperson')), ('login', '=', kwrgs.get('salesperson'))])
        
        if not customer:
            customer = partner_obj.sudo().create({"name": kwrgs.get('customer')})

        record["user_id"] = sales_person.id if sales_person else False
        record["partner_id"] = customer and customer.id
        
        try:
            lead = request.env['crm.lead'].sudo().create(record)
        except Exception as ex:
             _logger.exception('Error while creating lead!!.', ex)
        
        return {
            "id": lead.id
        }

