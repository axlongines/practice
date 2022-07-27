{
    "name": "openAcademy",
    "license": "LGPL-3",
    "summary": """This is a tecnical module where we can lear about odoo""",
    "author": "Vauxoo",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "15.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
        "views/course_view.xml",
        "views/course_menu_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": ["demo/course.xml"],
}
