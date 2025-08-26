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

__all__ = ['SALES_VP']
