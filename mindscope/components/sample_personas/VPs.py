from mindscope import Persona

SALES_VP = Persona(
    name="VP of Sales",
    description="A senior leader responsible for driving revenue growth and managing the sales organization.",
    goals=[
        "Achieve quarterly revenue targets",
        "Optimize sales processes and pipelines",
        "Motivate and enable sales teams",
        "Expand into new markets"
    ],
    pain_points=[
        "Unreliable pipeline forecasting",
        "Difficulty tracking team performance",
        "Customer churn in competitive markets"
    ],
    preferences={"tone": "motivational", "detail_level": "medium"},
    traits={"goal_focused": True, "time_sensitive": True, "people_oriented": True}
)

PRODUCT_HEAD = Persona(
    name="Head of Product",
    description="A business leader responsible for product vision, strategy, and execution across teams.",
    goals=[
        "Align product roadmap with business goals",
        "Prioritize customer needs and market trends",
        "Deliver features on time",
        "Balance innovation with stability"
    ],
    pain_points=[
        "Overwhelming feature requests",
        "Resource constraints across teams",
        "Difficulty balancing long-term strategy with short-term needs"
    ],
    preferences={"tone": "insightful", "detail_level": "medium"},
    traits={"tech_savvy": True, "goal_focused": True, "collaborative": True}
)


__all__ = ['SALES_VP', 'PRODUCT_HEAD']
