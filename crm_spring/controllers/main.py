from odoo import http
from odoo.addons.phone_validation.tools import phone_validation
from odoo.http import request

CRM_FIELDS = ['name', 'phone', 'customer', 'salesperson']


class CrmLeadController(http.Controller):

    @http.route("/lead", type='json', auth="public", methods=['POST'], csrf=False)
    def crm_lead_create(self, **kwrgs):
        print("kwrgs>>>>>>>>>>>>>>>>>>>>>>>>>", kwrgs)
        record = dict({})
        [ record.update({val: kwrgs.get(val, '')}) for val in CRM_FIELDS]
        print("record", record)
        # fmt_number = phone_validation.phone_format(
        #     number, contact_country.code if contact_country else None,
        #     contact_country.phone_code if contact_country else None,
        #     force_format='INTERNATIONAL',
        #     raise_exception=False
        # )
        # request.params.update({phone_field: fmt_number})
        
        return {}

