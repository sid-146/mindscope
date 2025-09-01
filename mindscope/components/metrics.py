"""
File to generate metrics according to persona.
"""

import json
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
        # Todo: Create prompt using summary, persona and no_of_metrics
        llm_client = llm(provider="openai")
        prompt = []
        # generating using default generation config
        response = llm_client.generate_text(prompt, MetricModel)
        # try to parse returned json string to MetricModel
        try:
            content = response.text[0].content
            content = json.loads(content)
            metrics = MetricModel(**content)
            self._metrics = metrics
        except Exception as e:
            raise e

        return metrics

    def update_definition(self, metric_name: str, instruction: str):
        raise NotImplementedError("Not Implemented yet.")
        if metric_name not in self._metrics:
            raise KeyError("Given metric not found in the current metric list.")

        # metric: MetricModel = self._metrics[metric_name]

        # Todo: Call llm and ask to update metric using given instruction
        return

    def remove_metric(self, metric_name: str):
        raise NotImplementedError("Not Implemented yet.")

    def iter_metrics(self):
        for metric in self._metrics.values():
            yield metric
