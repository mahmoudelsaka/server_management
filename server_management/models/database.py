from odoo import api, fields, models, _
from odoo.exceptions import Warning
import datetime
from odoo import SUPERUSER_ID

class DatabaseInfo(models.Model):
    _name = "database.info"
    _description = 'Database Information'
    _order = 'sequence'
    _inherit = ['mail.thread']

    @api.model
    def _default_user_id(self):
        return [self.env.context.get('uid'), SUPERUSER_ID]

    @api.one
    @api.depends('server_info_id')
    def _get_server_data(self):
        if self.server_info_id:
            self.version = self.server_info_id.version
            self.ip = self.server_info_id.ip

    name = fields.Char('Database Name', required=True)
    db_password = fields.Char('Database-Password', required=True, track_visibility='onchange')
    version = fields.Selection([('8','8.0'),('9','9.0'),('10','10.0'),
                                ('11','11.0'),('12','12.0'),('13','13.0')], 
                               string="Odoo Version", compute="_get_server_data", store=True)
    ip = fields.Char('IP', compute="_get_server_data", store=True)
    note = fields.Text('Note')
    sequence = fields.Integer('Sequence')
    server_info_id = fields.Many2one('server.info', 'Server', required=True, track_visibility='onchange')
    web_link = fields.Char('Web-Link', track_visibility='onchange')
    user_ids = fields.Many2many('res.users', 'database_user_rel', 'database_id', 
                                'user_id', 'Allowed Users', default=_default_user_id)

