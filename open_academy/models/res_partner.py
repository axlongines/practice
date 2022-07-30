from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean()
    level_1 = fields.Boolean()
    level_2 = fields.Boolean()
    teacher = fields.Boolean()
    instructor = fields.Boolean() 
    sessions_ids = fields.Many2many("open.academy.session", "res_partner_session_rel")
