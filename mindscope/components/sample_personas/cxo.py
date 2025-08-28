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

CHEIF_STRATEGY_OFFICER = Persona(
    name="Chief Strategy Officer",
    description="A C-level executive focused on long-term growth strategy, market positioning, and innovation.",
    goals=[
        "Identify new market opportunities",
        "Align corporate strategy with execution",
        "Ensure organization stays competitive",
        "Balance short-term performance with long-term growth"
    ],
    pain_points=[
        "Difficulty forecasting future market shifts",
        "Lack of alignment between strategy and execution",
        "Resource constraints in implementing vision"
    ],
    preferences={"tone": "visionary and concise", "detail_level": "low"},
    traits={"goal_focused": True, "innovation_driven": True, "big_picture_thinker": True}
)

CHEIF_INFORMATION_SECURITY_OFFICER = Persona(
    name="Chief Information Security Officer",
    description="A C-suite leader safeguarding organizational data, systems, and regulatory compliance.",
    goals=[
        "Protect against cyber threats",
        "Ensure regulatory and data compliance",
        "Educate employees on security practices",
        "Respond quickly to security incidents"
    ],
    pain_points=[
        "Rapidly evolving security threats",
        "Employee negligence in security protocols",
        "Pressure to prove ROI of cybersecurity investments"
    ],
    preferences={"tone": "urgent but professional", "detail_level": "low"},
    traits={"risk_averse": True, "detail_oriented": True, "proactive": True}
)


CHEIF_TECHNOLOGY_OFFICER = Persona(
    name="Chief Technology Officer",
    description="An executive overseeing technology strategy, innovation, and infrastructure scalability.",
    goals=[
        "Ensure scalable and secure tech infrastructure",
        "Adopt emerging technologies for business advantage",
        "Reduce downtime and technical debt",
        "Support innovation while managing costs"
    ],
    pain_points=[
        "Legacy system dependencies",
        "Cybersecurity threats",
        "Difficulty aligning tech with business priorities"
    ],
    preferences={"tone": "technical but strategic", "detail_level": "low"},
    traits={"tech_savvy": True, "risk_averse": True, "innovation_driven": True}
)



__all__ ['CHEIF_FINANCIAL_OFFICER', 'CHEIF_MARKETING_OFFICER', 'CHEIF_STRATEGY_OFFICER', 'CHEIF_INFORMATION_SECURITY_OFFICER','CHEIF_TECHNOLOGY_OFFICER' ]
