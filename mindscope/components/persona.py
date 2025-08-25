from typing import List, Dict


class Persona:
    def __init__(self, filepath):
        self.filepath = filepath
        self._name: str = None
        self._description: str = None
        self._goals: List[str] = None
        self._pain_points: List[str] = None
        self._preference: Dict[str, str] = {
            "tone": "trustworthy",
            "detail_level": "medium",
        }
        self._trait: Dict[str, str] = None

    @property
    def readable_file_formats(self):
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
    def preference(self):
        return self._preference

    @property.setter
    def preference(self, value):
        self._preference = value
