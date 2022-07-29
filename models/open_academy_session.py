from odoo import models, fields


class OpenAcademySession(models.Model):
    _name = "open.academy.session"
    _description = "model of session on open academy"

    name = fields.Char(required=True, size=50)
    duration = fields.Text()
    startDate = fields.Datetime()
    numberSeats = fields.Intger()
