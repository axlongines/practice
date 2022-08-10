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
    number_seats = fields.Integer(required=True)
    number_seats_taken = fields.Float(compute="_compute_number_taken_seats")
    instructor_id = fields.Many2one("res.partner", "instructor")
    course_id = fields.Many2one("open.academy.course", required=True)
    attendees_ids = fields.Many2many("res.partner", "session_res_partner_rel")
    attendees_count = fields.Integer(compute="_compute_number_taken_seats", store=True)


    @api.depends("number_seats", "attendees_ids")
    def _compute_number_taken_seats(self):
        for record in self:
            number_attenndees = len(record.attendees_ids)
            record.attendees_count = number_attenndees
            if number_attenndees == 0 or record.number_seats == 0:
                record.number_seats_taken = 0
            else:
                record.number_seats_taken = (number_attenndees / record.number_seats) * 100
        

    @api.onchange("number_seats", "attendees_ids")
    def _onchange_number_seats(self):
        if self.number_seats  < 0:
            return {
                "warning": {
                    "title": "Incorrect 'seats' value.",
                    "message": "The number of available seats may not be negative.",
                }
            }
        if len(self.attendees_ids) > self.number_seats:
            return {
                "warning": {
                    "title": "Too many attendees.",
                    "message": "There are more attendees than seats.",
                }
            }

    @api.constrains("instructor_id", "attendees_ids")
    def _check_instructor_id(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendees_ids:
                raise ValidationError("The instructor can't be also an attendee.")
