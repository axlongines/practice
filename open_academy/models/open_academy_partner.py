from odoo import models, fields


class OpenAcademyPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean()
    sessions_ids = fields.Many2many("open.academy.session", "instructor")
