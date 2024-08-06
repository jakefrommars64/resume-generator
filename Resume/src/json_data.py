import pathlib
import json
from utils import *


class Section:
    def __init__(self, layout: pathlib.Path):
        self.layout = layout.read_text()

    def get_formatted_layout(self, key, value):
        return replace_key(key, value, replace_key("section-id", key, self.layout))


class Profile:
    def __init__(self, data_path: pathlib.Path):
        self.path = data_path
        self.data = json.load(self.path.open())

    def get_skills(self):
        d = self.data["skills"]
        d.sort()
        print(d)
        return ", ".join(self.data["skills"])


class Contact:
    def __init__(self, data_path: pathlib.Path):
        self.path = data_path
        self.data = json.load(self.path.open())
        self.layout = '\n\n<img src="{$icon}" width="20"> <a class="resume-contact" href="{$data}">{$title}</a>'

    def get_formatted_layout(self):
        out = ""
        for contact in self.data:
            temp = self.layout
            if not contact["include"]:
                continue
            for key, value in contact.items():
                if key == "include":
                    continue
                temp = replace_key(key, value, temp)
            out += temp
        return out


class Education:
    def __init__(self, data_path: pathlib.Path, layout: pathlib.Path):
        self.path = data_path
        self.data = json.load(self.path.open())
        self.layout = layout.read_text()

    def get_formatted_layout(self):
        out = ""
        for institution in self.data:
            temp = self.layout
            if not institution["include"]:
                continue
            for key, value in institution.items():
                if key == "include":
                    continue
                if type(value) == list:
                    value = ", ".join(value)
                temp = replace_key(key, value, temp)
            out += "\n" + temp
        return out


class Certification(Education):
    def __init__(self, data_path: pathlib.Path, layout: pathlib.Path):
        super().__init__(data_path, layout)


class ProfessionalHistory:
    def __init__(
        self,
        data_path: pathlib.Path,
        layout: pathlib.Path,
        position_layout: pathlib.Path,
    ):
        self.path = data_path
        self.data = json.load(self.path.open())
        self.layout = layout.read_text()
        self.position_layout = position_layout.read_text()

    def get_formatted_layout(self):
        out = ""
        for employer in self.data:
            temp = replace_key("employer", employer["employer"], self.layout)
            temp_positions = ""
            for position in employer["positions"]:
                if not position["include"]:
                    continue
                temp_pos = self.position_layout
                for key, value in position.items():
                    if key == "include":
                        continue
                    if type(value) is list:
                        value = ", ".join(value)
                    temp_pos = replace_key(key, value, temp_pos)
                temp_positions += "\n" + temp_pos
            temp = replace_key("positions", temp_positions, temp)
            out += "\n" + temp

        return out


class Projects:
    def __init__(self, data_path: pathlib.Path, layout: pathlib.Path):
        self.path = data_path
        self.data = json.load(self.path.open())
        self.layout = layout.read_text()

    def get_formatted_layout(self):
        out = ""
        for project, data in self.data.items():
            if not data["include"]:
                continue
            temp = replace_key("project-name", project, self.layout)
            for key, value in data.items():
                if key == "include":
                    continue
                if type(value) is list:
                    value = ", ".join(value)
                temp = replace_key(key, value, temp)
            out += "\n::::: container resume\n" + temp + "\n:::::"

        return out
