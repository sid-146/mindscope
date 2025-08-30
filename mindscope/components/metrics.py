"""
File to generate metrics according to persona.
"""

from typing import Dict, List

from .models import MetricModel
from .persona import Persona
from .llm import llm

"""
What can be done
Metric versioning.
"""


class MetricsHandler:
    def __init__(self, summary: dict, persona: Persona):
        self._metrics: Dict[str, MetricModel] = {}

    @property
    def metrics_count(self):
        return len(self.metrics)

    @property
    def metrics(self) -> List[MetricModel]:
        return list(self._metrics.values())

    @property
    def metrics_names(self) -> List[str]:
        return list(self._metrics.keys())

    def generate_metrics(self, summary, persona, no_of_metrics: int = 5):
        """
        Generate metrics according to persona, and summary
        """
        # Todo: Call llm and ask to generate given number of metric, for summary and persona
        llm_client = llm(provider="openai")
        prompt = []

        return

    def update_definition(self, metric_name: str, instruction: str):
        if metric_name not in self._metrics:
            raise KeyError("Given metric not found in the current metric list.")

        metric: MetricModel = self._metrics[metric_name]

        # Todo: Call llm and ask to update metric using given instruction
        return
