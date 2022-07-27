from odoo import models, fields


class Course(models.Model):
    _name = "open.academy.course"
    _description = "model of courses on open academy"

    title = fields.Char(required=True, size=50)
    description = fields.Text()
