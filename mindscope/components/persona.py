from .core import FileNotSupportedError
from typing import List, Dict
from .utils.persona import from_json


class Persona:
    def __init__(self, name: str):
        self._name: str = name
        self._description: str = None
        self._goals: List[str] = None
        self._pain_points: List[str] = None
        self._preference: Dict[str, str] = {
            "tone": "trustworthy",
            "detail_level": "medium",
        }
        self._trait: Dict[str, str] = None
        self.readable_json_formats = ["json", "yaml"]

    def to_dict(self):
        return {
            "name": self._name,
            "description": self._description,
            "goals": self._goals,
            "pain_points": self._pain_points,
            "preference": self._preference,
            "trait": self._trait,
        }

    def __repr__(self):
        return f"Persona({self._name})"

    def __str__(self):
        return f"Persona({self._name})"

    # @property
    # def readable_file_formats(self):
    #     return ["json", "yaml"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value):
        self._goals = value

    @property
    def pain_points(self):
        return self._pain_points

    @pain_points.setter
    def pain_points(self, value):
        self._pain_points = value

    @property
    def preferences(self):
        return self._preference

    @preferences.setter
    def preferences(self, value):
        self._preference = value

    @staticmethod
    def from_file_path(path: str):
        extn = path.split(".")[-1]
        if extn.lower() in ["json", "yaml"]:
            if extn.lower() == "json":
                data: dict = from_json(path)
        else:
            raise FileNotSupportedError("Given file format is not supported.")
        try:
            if name := data.get("name"):
                persona = Persona(name=name)
            else:
                raise AttributeError("Persona Should be initialized with the name.")

            persona.description = data.get("description")
            persona.goals = data.get("goals")
            persona.pain_points = data.get("pain_points")
            persona.preferences = data.get("preferences")

            return persona
        except Exception as e:
            raise e
