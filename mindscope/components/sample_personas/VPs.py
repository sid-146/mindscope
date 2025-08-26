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


BUSINESS_HEAD = Persona(
    name="Business Unit Head",
    description="A leader accountable for the P&L, operations, and strategy of a specific business unit.",
    goals=[
        "Grow revenue in the business unit",
        "Optimize operations and efficiency",
        "Align business unit strategy with corporate goals",
        "Develop competitive advantage in the market"
    ],
    pain_points=[
        "Conflicting priorities between units",
        "Limited resources vs growth expectations",
        "Market competition pressures"
    ],
    preferences={"tone": "strategic", "detail_level": "medium"},
    traits={"goal_focused": True, "data_driven": True, "competitive": True}
)

DIRECTOR_OF_OPS = Persona(
    name="Director of Operations",
    description="A senior manager ensuring smooth day-to-day business operations and process optimization.",
    goals=[
        "Improve operational efficiency",
        "Minimize downtime and bottlenecks",
        "Implement cost-saving initiatives",
        "Maintain high customer satisfaction"
    ],
    pain_points=[
        "Inefficient processes",
        "Poor cross-team communication",
        "Difficulty measuring productivity in real-time"
    ],
    preferences={"tone": "practical", "detail_level": "medium"},
    traits={"organized": True, "time_sensitive": True, "risk_averse": True}
)



__all__ = ['SALES_VP', 'PRODUCT_HEAD', 'BUSINESS_HEAD', 'DIRECTOR_OF_OPS']


