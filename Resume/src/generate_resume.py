import pathlib
import json
from json_data import ProfessionalHistory, Projects
import os
from utils import *


def run():
    professional_history = ProfessionalHistory(
        PATH_PROFESSIONAL_HISTORY_DATA,
        PATH_PROFESSIONAL_HISTORY_LAYOUT,
        PATH_PROFESSIONAL_HISTORY_POSITION_LAYOUT,
    ).get_formatted_layout()
    projects = Projects(PATH_PROJECTS_DATA, PATH_PROJECTS_LAYOUT).get_formatted_layout()

    resume = PATH_MAIN_LAYOUT.read_text()
    resume = replace_key("professional-history", professional_history, resume)
    resume = replace_key("projects", projects, resume)

    out = PATH_OUT
    out.parent.mkdir(exist_ok=True)
    out.write_text(resume)


if __name__ == "__main__":
    run()
