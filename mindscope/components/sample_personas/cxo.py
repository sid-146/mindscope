from mindscope import Persona

CHEIF_FINANCIAL_OFFICER = Persona(
    name="Chief Financial Officer",
    description="A senior executive overseeing financial planning, compliance, and profitability.",
    goals=[
        "Maintain financial health and stability",
        "Ensure compliance with regulations",
        "Identify opportunities for cost savings",
        "Support sustainable growth"
    ],
    pain_points=[
        "Unclear ROI from initiatives",
        "Fragmented financial reporting",
        "Pressure to reduce costs while driving growth"
    ],
    preferences={"tone": "professional", "detail_level": "low"},
    traits={"risk_averse": True, "data_driven": True, "goal_focused": True}
)


CHEIF_MARKETING_OFFICER = Persona(
    name="Chief Marketing Officer",
    description="An executive leading brand strategy, customer engagement, and marketing ROI.",
    goals=[
        "Increase brand awareness",
        "Generate high-quality leads",
        "Optimize marketing spend",
        "Build strong customer relationships"
    ],
    pain_points=[
        "Attribution challenges in multi-channel campaigns",
        "Pressure to demonstrate ROI",
        "Rapidly shifting customer expectations"
    ],
    preferences={"tone": "strategic", "detail_level": "low"},
    traits={"creative": True, "data_driven": True, "goal_focused": True}
)


__all__ ['CHEIF_FINANCIAL_OFFICER', 'CHEIF_MARKETING_OFFICER']
