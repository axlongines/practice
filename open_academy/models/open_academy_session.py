from odoo import models, fields


class OpenAcademySession(models.Model):
    _name = "open.academy.session"
    _description = "model of session on open academy"

    name = fields.Char(required=True, size=50)
    duration = fields.Text()
    start_date = fields.Datetime()
    number_seats = fields.Integer()
    instructor_id = fields.Many2one("res.partner", "instructor")
    course_id = fields.Many2one("open.academy.course", required=True)
    attendees_ids = fields.Many2many("res.partner", "session_res_partner_rel")
