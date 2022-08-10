from odoo import models, fields


class OpenAcademyWizard(models.TransientModel):
    _name = "open.academy.wizard"
    _description = "wizard model on open academy"


    session_id = fields.Many2many("open.academy.session", 'open_academy_wizard_open_academy_session_rel',
                                  string="Sessions", default=lambda self: self._default_session_id())
    attendee_ids = fields.Many2many('res.partner', 'open_academy_wizard_res_partner_rel', string="Attendees")

    def _default_session_id(self):
        return self.env['open.academy.session'].browse(self._context.get('active_ids'))

    def add_attendees(self):
        for session in self.session_id:
            session.attendee_ids |= self.attendee_ids
