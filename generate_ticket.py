from jinja2 import Environment, FileSystemLoader, Template
from weasyprint import HTML
from models.participant import Participant
from typing import List
import os


TEMPLATE_PATH = "templates/general_pass_template.html"
TICKETS_PATH = "output"


class TicketGenerator:

    def __init__(self, participants: List[Participant]):
        self.participants: List[Participant] = participants
        self.ticket_template: Template = self.load_template()
        self.generated_file_path: str = ""

    def load_template(self) -> Template:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(TEMPLATE_PATH)
        return template

    def generate_file_path(self, participant: Participant) -> str:
        name = participant.name.strip().replace(" ", "_")
        id = participant.id
        participant_ticket_file_name = f"{id}_{name}.pdf"
        filepath = os.path.join(TICKETS_PATH, participant_ticket_file_name)
        return filepath

    def generate_ticket_for_participant(self, participant: Participant):
        rendered_html: str = self.ticket_template.render(ticket=participant.model_dump())
        os.makedirs(TICKETS_PATH, exist_ok=True)

        file_path = self.generate_file_path(participant)
        HTML(string=rendered_html).write_pdf(file_path)
        self.generated_file_path = file_path

    def run(self) -> None:
        for participant in self.participants:
            self.generate_ticket_for_participant(participant)
