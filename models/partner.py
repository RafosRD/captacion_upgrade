from openerp import models, fields, api,exceptions

class captacion_upgrade_res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'


    @api.model
    def create(self, vals):

        if  vals['catchment_id'] == False:
            raise exceptions.ValidationError('Debe que agregar un metodo de captura')

        return super(captacion_upgrade_res_partner, self).create(vals)
