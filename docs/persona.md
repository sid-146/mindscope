## 🧱 Basic Persona Structure (Python)

```python
from mindscope import Persona

persona = Persona(
    name="Persona Name",
    description="Brief bio or summary of the persona",
    goals=["Goal 1", "Goal 2"],
    pain_points=["Pain point 1", "Pain point 2"],
    preferences={"tone": "insightful", "detail_level": "high"},
    traits={"tech_savvy": True, "time_sensitive": False}
)
```

---

## 🎯 Example Personas

### 1. **Eco-Conscious Shopper** (Retail, Sustainability)

```python
persona = Persona(
    name="Eco-Conscious Shopper",
    description="A consumer who prioritizes sustainability, ethical sourcing, and low environmental impact.",
    goals=[
        "Reduce carbon footprint",
        "Support eco-friendly brands",
        "Avoid greenwashing"
    ],
    pain_points=[
        "Lack of transparency in supply chains",
        "Overwhelming product choices",
        "Difficulty identifying authentic sustainable products"
    ],
    preferences={"tone": "trustworthy", "detail_level": "medium"},
    traits={"budget_sensitive": True, "research_oriented": True}
)
```

---

### 2. **Busy Product Manager** (SaaS, B2B)

```python
persona = Persona(
    name="Busy Product Manager",
    description="A product lead juggling feature planning, team coordination, and stakeholder updates.",
    goals=[
        "Make data-driven decisions quickly",
        "Communicate insights clearly to the team",
        "Align roadmap with business goals"
    ],
    pain_points=[
        "Too much unstructured data",
        "Time constraints",
        "Overwhelming analytics tools"
    ],
    preferences={"tone": "concise", "detail_level": "low"},
    traits={"tech_savvy": True, "visual_learner": True}
)
```

---

### 3. **First-Time Job Seeker** (HR, Career)

```python
persona = Persona(
    name="First-Time Job Seeker",
    description="A recent graduate exploring the job market and looking for guidance.",
    goals=[
        "Find relevant entry-level opportunities",
        "Improve resume and interviewing skills",
        "Understand industry expectations"
    ],
    pain_points=[
        "Lack of work experience",
        "Unclear job requirements",
        "Overwhelming job platforms"
    ],
    preferences={"tone": "encouraging", "detail_level": "high"},
    traits={"tech_savvy": True, "goal_focused": True}
)
```

---

## 📄 Persona as JSON (Optional External File)

You could also define personas externally like this:

```json
{
  "name": "Eco-Conscious Shopper",
  "description": "A consumer who prioritizes sustainability, ethical sourcing, and low environmental impact.",
  "goals": [
    "Reduce carbon footprint",
    "Support eco-friendly brands",
    "Avoid greenwashing"
  ],
  "pain_points": [
    "Lack of transparency in supply chains",
    "Overwhelming product choices",
    "Difficulty identifying authentic sustainable products"
  ],
  "preferences": {
    "tone": "trustworthy",
    "detail_level": "medium"
  },
  "traits": {
    "budget_sensitive": true,
    "research_oriented": true
  }
}
```

You could then load it like:

```python
persona = Persona.from_json("personas/eco_shopper.json")
```
