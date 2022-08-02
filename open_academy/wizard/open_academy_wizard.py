from odoo import models, fields


class OpenAcademyWizard(models.TransientModel):
    _name = "open.academy.wizard"
    _description = "wizard model on open academy"

    sessions_id = fields.Many2one("open.academy.session", string='open_academy_wizard_open_academy_session_rel')
    partners_ids = fields.Many2many('res.partner', string='open_academy_wizard_res_partner_rel')