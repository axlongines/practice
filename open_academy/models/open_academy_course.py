from odoo import models, fields


class OpenAcademyCourse(models.Model):
    _name = "open.academy.course"
    _description = "model of courses on open academy"

    title = fields.Char(required=True, size=50)
    description = fields.Text()
    responsible_id = fields.Many2one("res.users")
    sessions_ids = fields.One2many("open.academy.session", "course_id")

    _sql_constraints = [
        ("title_description_diferents", "check(title!=description)",
        "the title and the description must be diferents"),("title_unique", "unique(title)",
        "this course title is already taken "),
    ]

    def copy(self, default=None):
        if default == None:
            default = {}
        default["title"] = self.title + " copy"
        rtn = super(OpenAcademyCourse, self).copy(default=default)
        return rtn
