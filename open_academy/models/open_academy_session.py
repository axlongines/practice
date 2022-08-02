from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OpenAcademySession(models.Model):
    _name = "open.academy.session"
    _description = "model of session on open academy"

    name = fields.Char(required=True, size=50)
    duration = fields.Integer()
    active = fields.Boolean(default=True)
    start_date = fields.Datetime(default=fields.Date.context_today)
    end_date = fields.Datetime()
    number_seats = fields.Integer(default=50, required=True)
    number_seats_taken = fields.Integer()
    instructor_id = fields.Many2one("res.partner", "instructor")
    course_id = fields.Many2one("open.academy.course", required=True)
    attendees_ids = fields.Many2many("res.partner", "session_res_partner_rel")
    available_seats_computed = fields.Integer(compute="percentage_computed")

    @api.depends("number_seats", "number_seats_taken")
    def percentage_computed(self):
        for records in self:
            available = records.number_seats - records.number_seats_taken
            records.available_seats_computed = (available / records.number_seats) * 100

    @api.onchange("number_seats_taken")
    def _onchange_number_seats_taken(self):
        if self.number_seats_taken > self.number_seats:
            return {
                "warning": {
                    "title": "Over atendance",
                    "message": "There are more atendances than seats",
                }
            }

    @api.onchange("number_seats")
    def _onchange_number_seats(self):
        if self.number_seats < 0:
            return {
                "warning": {
                    "title": "Unavailable negative seats",
                    "message": "Can't have less than 0 seats",
                }
            }

    @api.constrains("instructor_id")
    def _constrains_instructor_id(self):
        for record in self:
            attendances_list_id = self.attendees_ids.mapped("id")
            if record.instructor_id.id in attendances_list_id:
                raise ValidationError("The instructor can't be also an attendance")
