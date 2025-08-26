from core import FileNotSupportedError
from typing import List, Dict
from persona_helper import from_json


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

    @property
    def readable_file_formats():
        return ["json", "yaml"]

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @property.setter
    def description(self, value):
        self._description = value

    @property
    def goals(self):
        return self._goals

    @property.setter
    def goals(self, value):
        self._goals = value

    @property
    def pain_points(self):
        return self._pain_points

    @property.setter
    def pain_points(self, value):
        self._pain_points = value

    @property
    def preferences(self):
        return self._preference

    @property.setter
    def preferences(self, value):
        self._preference = value

    @staticmethod
    def from_file_path(path: str):
        extn = path.split(".")[-1]
        if extn.lower() in Persona.readable_file_formats:
            if extn.lower() == "json":
                data: dict = from_json(path)
        else:
            raise FileNotSupportedError("Given file format is not supported.")
        try:
            persona = Persona()
            if name := data.get("name"):
                persona.name = name
            else:
                raise AttributeError("Persona Should be initialized with the name.")

            persona.description = data.get("description")
            persona.goals = data.get("goals")
            persona.pain_points = data.get("pain_points")
            persona.preferences = data.get("preferences")
        except Exception as e:
            raise e
