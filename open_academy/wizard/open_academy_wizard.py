from email.policy import default
from odoo import models, fields


class OpenAcademyWizard(models.TransientModel):
    _name = "open.academy.wizard"
    _description = "wizard model on open academy"


    def _default_sessions(self):
        return self.env['open.academy.session'].browse(self._context.get('active_ids'))


    sessions_id = fields.Many2many("open.academy.session", string='open_academy_wizard_open_academy_session_rel',default=_default_sessions)
    attendees_ids = fields.Many2many('res.partner', string='open_academy_wizard_res_partner_rel')

    def add_partners(self):
        for session in self.sessions_id:
            session.attendees_ids |= self.attendees_ids