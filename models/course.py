from odoo import models, fields


class Course(models.Model):
    _name = "open_academy.course"
    _description = "Test course"

    title = fields.Char(required=True, size=50)
    description = fields.Text()
