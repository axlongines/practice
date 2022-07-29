from odoo import models, fields


class OpenAcademySession(models.Model):
    _name = "open.academy.session"
    _description = "model of session on open academy"

    name = fields.Char(required=True, size=50)
    duration = fields.Text()
    startDate = fields.Datetime()
    numberSeats = fields.Integer()
    instructor = fields.Many2one("res.partner")
    course = fields.Many2one("open.academy.course", required=True)
