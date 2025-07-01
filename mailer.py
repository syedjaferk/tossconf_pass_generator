import smtplib
from email.message import EmailMessage
from models.email import Email
from jinja2 import Environment, FileSystemLoader, Template

TEMPLATE_PATH = "templates/email_template.html"


class Emailer:
    def __init__(self, email: Email):
        self.message = EmailMessage()
        self.email = email
        self.ticket_template: Template = self.load_template()
    
    def load_template(self) -> Template:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(TEMPLATE_PATH)
        return template
    
    def render_html(self):
        self.email.html_body = self.ticket_template.render(ticket={"name": self.email.receiver_name})

    def set_message(self):
        self.message['From'] = self.email.from_mail_id
        self.message['To'] = self.email.to_mail_id
        self.message['Subject'] = self.email.subject
        self.message.set_content("This email requires an HTML viewer.")
        self.message.add_alternative(self.email.html_body, subtype='html')

    def add_attachements(self):
        if self.email.attachments:
            for file_path in self.email.attachments:
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = file_path.split("/")[-1]
                    self.message.add_attachment(file_data,
                                       maintype='application',
                                       subtype='octet-stream',
                                       filename=file_name)

    def send_mail(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email.from_mail_id, self.email.app_password.get_secret_value())
            smtp.send_message(self.message)

    def run(self):
        self.load_template()
        self.render_html()
        self.set_message()
        self.add_attachements()
        self.send_mail()
