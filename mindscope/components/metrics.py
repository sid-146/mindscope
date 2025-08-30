"""
File to generate metrics according to persona.
"""

from .models import MetricModel


class Metric:
    def __init__(self, metric: MetricModel):
        self._metric = metric
        self._name = metric.name
        self._definition = metric.definition
        self._importance = metric.importance
        self._formula = metric.formula
        self._steps = metric.steps
        self._code_string = metric.code_string

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._metric.name = value
        self._name = value

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        self._metric.definition = value
        self._definition = value

    @property
    def importance(self):
        return self._importance

    @importance.setter
    def importance(self, value):
        self._metric.importance = value
        self._importance = value

    @property
    def formula(self):
        return self._formula

    @formula.setter
    def formula(self, value):
        self._metric.formula = value
        self._formula = value

    @property
    def calculation_steps(self):
        return self._steps

    def update_definition_using_instruction(self, instruction):
        """
        Function takes instruction and updates the metric definition and other attributes.

        :params:
        instruction: str
        """
        # Todo
        # call llm with instruction to update metric definition
        # Do we need to update all the attributes
        return
