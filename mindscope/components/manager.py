"""
Todo:
    - Update file structure
    - Add logic to handle multiple persona: ps manager part is easy but how to handle goals and other feature for multiple persona is challenging thus skipping for now.
"""

import polars as pl

from .core import EMPTY_DF
from .utils.manager import get_dataframe_from_filepath
from .summarizer import Summarizer
from .persona import Persona


class Manager:
    """
    Manager Responsible for execution of different components.
    Managers handles a single file at a time.
    Responsible for data loading and checking for empty dataframes.

    - Components:
        - Summarizer
    """

    def __init__(self, data: pl.DataFrame = EMPTY_DF, filepath: str = ""):
        """
        Takes dataframe or file_path as argument if both given then dataframe will be prioritized.

        Requires tabular format for now.
        """
        if isinstance(data, pl.DataFrame):
            self._data = data
        elif filepath:
            self._data = get_dataframe_from_filepath(filepath)
            self._filepath = filepath
        else:
            raise ValueError("Either data or filepath must be provided.")
        self._data = data
        self._filepath = filepath
        self.summarizer: Summarizer = None
        self.persona: Persona = None
        # self.personas: Dict[str, Persona] = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def summarize(self, n_samples=5, enrich=False):
        """
        Docstring will go here

        :param: enrich
        bool : Set true to use it for

        """
        if self.data.is_empty():
            raise ValueError(
                "Please provider data to summarize. Assign Manager a dataset."
            )
        if not self.summarizer:
            self.summarizer = Summarizer(self.data)

        summary = self.summarizer.summarize(n_samples=n_samples, enrich=enrich)
        return summary

    def set_persona(self, persona: Persona) -> None:
        """
        Given persona.
        """
        if not persona.name:
            raise AttributeError("Persona should have name.")

        self.persona = persona

        # if persona.name.lower() in self.personas.keys():
        #     self.personas[persona.name.lower()] = persona
        # else:
        #     self.personas[persona.name.lower()] = persona

    # def set_personas(self, personas: List[Persona]) -> None:
    #     for persona in personas:
    #         if not persona.name:
    #             raise AttributeError("Persona name not found.")

    #     update_dict = {persona.name: persona for persona in personas}
    #     self.personas.update(update_dict)
