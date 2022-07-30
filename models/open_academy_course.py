from odoo import models, fields


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "model of courses on open academy"

    title = fields.Char(required=True, size=50)
    description = fields.Text()
    responsible = fields.Many2one("res.users")
    sessions = fields.One2many("open.academy.session", "course")
