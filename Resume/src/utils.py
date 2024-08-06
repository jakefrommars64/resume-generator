import os
import pathlib
import re

REPLACEMENT_IDENTIFIER = "\{\$key\}"


def replace_key(key: str, value: str, txt: str):
    return re.sub(REPLACEMENT_IDENTIFIER.replace("key", key), value, txt)


dir_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)).replace("src", ""))
PATH_OUT = dir_path.joinpath("out/resume.md")

PATH_CONTACT_DATA = dir_path.joinpath("data/contact.json")
PATH_PROFESSIONAL_HISTORY_DATA = dir_path.joinpath("data/professional-history.json")
PATH_PROJECTS_DATA = dir_path.joinpath("data/projects.json")

PATH_SECTION_LAYOUT = dir_path.joinpath("layout/section.md")
PATH_MAIN_LAYOUT = dir_path.joinpath("layout/main.md")
PATH_PROFESSIONAL_HISTORY_LAYOUT = dir_path.joinpath("layout/professional-history.md")
PATH_PROFESSIONAL_HISTORY_POSITION_LAYOUT = dir_path.joinpath(
    "layout/professional-history-position.md"
)
PATH_PROJECTS_LAYOUT = dir_path.joinpath("layout/projects.md")
