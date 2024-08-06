import pathlib
import json
from json_data import *
import os
from utils import *


def run():
    section = Section(PATH_SECTION_LAYOUT)
    contact = Contact(PATH_CONTACT_DATA).get_formatted_layout()

    professional_history = ProfessionalHistory(
        PATH_PROFESSIONAL_HISTORY_DATA,
        PATH_PROFESSIONAL_HISTORY_LAYOUT,
        PATH_PROFESSIONAL_HISTORY_POSITION_LAYOUT,
    ).get_formatted_layout()
    projects = Projects(PATH_PROJECTS_DATA,
                        PATH_PROJECTS_LAYOUT).get_formatted_layout()

    resume = PATH_MAIN_LAYOUT.read_text()
    resume = replace_key("contact", contact, resume)

    sections = {"projects": projects,
                "professional-history": professional_history}
    for key, value in sections.items():
        resume += section.get_formatted_layout(key, value)

    out = PATH_OUT
    out.parent.mkdir(exist_ok=True)
    out.write_text(resume)


if __name__ == "__main__":
    run()
