import pathlib
import json
from utils import *


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
                if key == "project-categories":
                    value = ", ".join(value)
                temp = replace_key(key, value, temp)
            out += "\n" + temp

        return out

        return out
