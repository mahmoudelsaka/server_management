from odoo import api, fields, models, _
from odoo.exceptions import Warning
import datetime
from odoo import SUPERUSER_ID

class ServerInfo(models.Model):
    _name = "server.info"
    _description = 'Server Information'
    _order = 'sequence'
    _inherit = ['mail.thread']

    @api.one
    @api.depends('ip', 'ssh_user')
    def _make_ssh_command(self):
        if self.ip and self.ssh_user:
            self.ssh_command = self.ssh_user + '@' + self.ip
        else:
            self.ssh_command = False

    @api.model
    def _default_user_id(self):
        return [self.env.context.get('uid'), SUPERUSER_ID]

    sequence = fields.Integer('Sequence')
    name = fields.Char('Server Name', required=True)
    version = fields.Selection([('8','8.0'),('9','9.0'),('10','10.0'),
                                ('11','11.0'),('12','12.0'),('13','13.0')], 
                               string="Odoo Version", required=True)
    ip = fields.Char('Server-IP', required=True, track_visibility='onchange')
    ssh_user = fields.Char('SSH-User', required=True, track_visibility='onchange')
    ssh_password = fields.Char('SSH-Password', required=True, track_visibility='onchange')
    master_password = fields.Char('Master-Password', required=True, track_visibility='onchange')
    ip_type = fields.Selection([('public','Public IP'), ('static', 'Static IP')], 
                               string="Type", default=lambda *a: 'public')
    ssh_command = fields.Char('SSH', compute="_make_ssh_command")
    inhouse = fields.Boolean('In-house', default=lambda *a: False)
    note = fields.Text('Note')

    user_ids = fields.Many2many('res.users', 'server_user_rel', 'server_id', 
                                'user_id', 'Allowed Users', default=_default_user_id)