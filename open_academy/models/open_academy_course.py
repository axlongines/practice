from odoo import models, fields, _


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "model of courses on open academy"

    title = fields.Char(required=True, size=50)
    description = fields.Text()
    responsible_id = fields.Many2one("res.users")
    sessions_ids = fields.One2many("open.academy.session", "course_id")

    _sql_constraints = [
        ("title_description_different", "CHECK(title!=description)",
         _("The title and description must be different.")),
        ("title_unique", "UNIQUE(title)",
         _("This course title is already taken.")),
    ]

    def copy(self, default=None):
        if default is None:
            default = {}
        default["title"] = _("Copy of ") + self.title
        return super().copy(default=default)
