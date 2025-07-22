# 🧠 `Persona` Object – Key Fields Explained

A persona in mindscope is a structured representation of a specific user, audience, or stakeholder type. It captures their goals, motivations, pain points, and expectations — forming the basis for how data is interpreted. Rather than treating all data equally, mindscope asks: What would this persona care about most? This allows the analysis to be more focused, relevant, and actionable. By embedding personas, your insights become context-aware and tailored to real human needs.

---

### 🔹 `name` (str)

**What it is:**
A short, descriptive name for the persona.

**Example:**

```python
name = "Eco-Conscious Shopper"
```

**Why it matters:**
Gives your persona an identity and makes it easy to reference in reports, visualizations, and logs.

---

### 🔹 `description` (str)

**What it is:**
A brief paragraph or sentence summarizing who this persona is — their role, mindset, and context.

**Example:**

```python
description = "A consumer who prioritizes sustainability, ethical sourcing, and low environmental impact."
```

**Why it matters:**
Provides human-readable context. Helps clarify the point of view being applied to data analysis.

---

### 🔹 `goals` (List\[str])

**What it is:**
A list of key objectives or outcomes this persona is trying to achieve.

**Example:**

```python
goals = ["Reduce carbon footprint", "Support eco-friendly brands"]
```

**Why it matters:**
The engine uses goals to filter and prioritize what data insights are most relevant to the persona.

---

### 🔹 `pain_points` (List\[str])

**What it is:**
Challenges, frustrations, or obstacles that commonly affect this persona.

**Example:**

```python
pain_points = ["Greenwashing", "Too much choice", "Lack of transparency"]
```

**Why it matters:**
These help the insight engine detect risk areas, data signals of dissatisfaction, or blockers.

---

### 🔹 `preferences` (Dict\[str, str])

**What it is:**
Communication and formatting preferences: tone, level of detail, style, or output format.

**Common keys:**

- `tone`: `"trustworthy"`, `"concise"`, `"insightful"`, `"encouraging"`, etc.
- `detail_level`: `"low"`, `"medium"`, `"high"`

**Example:**

```python
preferences = {"tone": "insightful", "detail_level": "medium"}
```

**Why it matters:**
Guides how reports or summaries are worded and presented for that persona.

---

### 🔹 `traits` (Dict\[str, Any])

**What it is:**
A flexible dictionary of personality, behavior, or decision-making traits.

**Common keys:**

- `tech_savvy`: `True` or `False`
- `risk_averse`: `True`
- `visual_learner`: `True`
- `goal_focused`: `True`
- `budget_sensitive`: `True`

**Example:**

```python
traits = {"tech_savvy": True, "budget_sensitive": True}
```

**Why it matters:**
These traits can influence how data is interpreted — e.g., whether the persona prefers quick overviews, visualizations, or detailed breakdowns.

---

### Optional Additional Fields You Can Support:

| Field                | Type        | Purpose                                                                                 |
| -------------------- | ----------- | --------------------------------------------------------------------------------------- |
| `experience_level`   | `str`       | e.g. `"beginner"`, `"expert"` – influences assumed data literacy                        |
| `industry`           | `str`       | Helps contextualize insights within specific domains                                    |
| `values`             | `List[str]` | e.g. `"sustainability"`, `"efficiency"`, `"trust"` – can guide tone and recommendations |
| `metrics_of_success` | `List[str]` | What success looks like for the persona (used to validate if goals are being met)       |

---

## ✅ Summary

| Key           | Type             | Description                              |
| ------------- | ---------------- | ---------------------------------------- |
| `name`        | `str`            | Persona's title or role                  |
| `description` | `str`            | Short bio or context                     |
| `goals`       | `List[str]`      | What they’re trying to achieve           |
| `pain_points` | `List[str]`      | Their frustrations or blockers           |
| `preferences` | `Dict[str, str]` | How they prefer to receive insights      |
| `traits`      | `Dict[str, Any]` | Behavioral flags to personalize analysis |

---


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
