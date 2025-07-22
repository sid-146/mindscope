# 🧠 mindscope

**mindscope** is a Python library that helps you analyze data **from the perspective of a defined persona** — enabling deeper, goal-aligned insights and decision-making. Instead of generic summaries, `mindscope` tailors its analysis to what *matters* most to your target audience, user type, or stakeholder persona.

---

## 🔍 What It Does

Using a provided **persona profile**, `mindscope` interprets your data with human-like context. It produces:

* 🎯 **Persona-aligned Insights** – What matters most *to this persona* in the dataset?
* 🧠 **Goal-Based Inference** – How does the data help or hinder the persona’s goals?
* 📊 **Visual Narratives** – Charts and summaries customized for persona-driven analysis
* 📝 **Narrative Reports** – Human-readable summaries filtered through persona needs and expectations

---

## 💡 Why Use `mindscope`?

In product design, marketing, UX, and strategy, it’s not just about *what the data says*, but *who you're looking at it for*.

Traditional analysis is one-size-fits-all. `mindscope` makes it personal.

---

## 📦 Installation

```bash
pip install mindscope
```

---

## 🧪 Quick Start

```python
from mindscope import Persona, InsightEngine

# Define the persona
persona = Persona(
    name="Eco-conscious Shopper",
    goals=["Reduce carbon footprint", "Buy sustainable products"],
    pain_points=["Greenwashing", "Lack of transparency"]
)

# Analyze external data through the persona lens
engine = InsightEngine(data_path="data/retail_data.csv", persona=persona)

# Generate insights, summaries, and visual reports
summary = engine.generate_summary()
insights = engine.generate_insights()
engine.visualize()

print(summary)
```

---

## 🎯 Use Cases

* **Product & UX Teams** – Evaluate how well your data supports key user personas
* **Marketing & Campaigns** – Tailor messaging based on persona-focused insights
* **HR or Learning Platforms** – Align content recommendations with individual or archetype personas
* **Consulting & Research** – Deliver custom reports for different stakeholder types

---

## 📁 Supported Input Formats

* CSV, JSON, XLSX (data files)
* JSON or Python-defined `Persona` objects

---

## 🧠 Philosophy

> **Context matters.**
> Data is only meaningful when interpreted through the lens of who it affects.

`mindscope` puts the *persona first* — so your insights are targeted, relevant, and human-centric.

---

## 📚 Documentation

📖 Coming soon: [https://your-link-here.com](https://your-link-here.com)  
Explore usage examples in the `/examples/` folder.

---

## 🛠️ License

MIT License
Contributions welcome – see `CONTRIBUTING.md`
