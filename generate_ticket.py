from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

ticket_data = {
    "id": "T25-G-00122",
    "type": "General Pass",
    "name": "Syed Jafer K",
    "email": "Contact.syedjafer@gmail.com",
    "phone": "9176409201"
}

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("general_pass_template.html")
rendered_html = template.render(ticket=ticket_data)

HTML(string=rendered_html).write_pdf("sample_ticket.pdf")
