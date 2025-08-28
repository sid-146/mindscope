# 🔹 End-to-End Persona Example (Finance)

---

## 🧑 Persona Definition

### **Persona: Retail Banking CXO (Chief Customer Officer)**

```python
persona = Persona(
    name="Chief Customer Officer - Retail Banking",
    description="An executive overseeing customer experience and growth in a retail bank. Focused on reducing churn, improving customer lifetime value, and driving adoption of digital channels.",
    goals=[
        "Reduce customer churn",
        "Increase cross-sell and upsell opportunities",
        "Improve digital adoption rates",
        "Enhance customer satisfaction (NPS, CSAT)"
    ],
    pain_points=[
        "High churn among younger demographics",
        "Low engagement with mobile banking apps",
        "Fragmented customer feedback data",
        "Difficulty aligning KPIs with financial outcomes"
    ],
    preferences={"tone": "insightful", "detail_level": "medium"},
    traits={"data_driven": True, "visual_learner": True, "goal_focused": True}
)
```

---

## 📊 Example Dataset

Imagine the bank collects **monthly customer data**:

| customer\_id | age\_group | account\_type | churned | monthly\_transactions | mobile\_app\_logins | cross\_products | satisfaction\_score |
| ------------ | ---------- | ------------- | ------- | --------------------- | ------------------- | --------------- | ------------------- |
| 1001         | 18-25      | Savings       | Yes     | 5                     | 2                   | 1               | 6                   |
| 1002         | 26-35      | Checking      | No      | 25                    | 12                  | 3               | 8                   |
| 1003         | 36-50      | Savings       | No      | 15                    | 5                   | 2               | 7                   |
| 1004         | 18-25      | Credit Card   | Yes     | 3                     | 0                   | 1               | 5                   |
| 1005         | 51+        | Savings       | No      | 20                    | 1                   | 2               | 9                   |

*(This is just a toy dataset; in reality, it could have millions of rows.)*

---

## 🎯 Persona-Aligned Goals (from the dataset)

### 1. **Reduce Customer Churn**

* Metric: % of customers who churned (left the bank).
* Goal: Identify high-risk groups (e.g., younger customers).

### 2. **Increase Cross-Sell/Upsell**

* Metric: Average number of products per customer (`cross_products`).
* Goal: Spot low-engagement groups and design offers.

### 3. **Improve Digital Adoption**

* Metric: Mobile app logins vs total transactions.
* Goal: Track digital adoption by age group.

### 4. **Enhance Customer Satisfaction**

* Metric: Average `satisfaction_score`.
* Goal: Detect where poor satisfaction overlaps with churn.

---

## 📈 Visualizations That Support Persona’s Goals

Here’s how each goal translates into visuals that your module could generate:

---

### 1. Churn Analysis

* **Visualization:** Bar chart of churn rate (%) by age group.
* **Insight:** Younger demographics (18–25) have higher churn, indicating need for targeted retention campaigns.

---

### 2. Cross-Sell & Upsell

* **Visualization:** Boxplot or histogram of `cross_products` across customer segments.
* **Insight:** Checking account holders average 3 products, but savings account holders average only 1–2 → upsell opportunity.

---

### 3. Digital Adoption

* **Visualization:** Line or stacked bar chart comparing **mobile\_app\_logins** vs **monthly\_transactions** by age group.
* **Insight:** Older customers transact often but rarely use the mobile app → need for digital training campaigns.

---

### 4. Satisfaction & Churn

* **Visualization:** Scatter plot of **satisfaction\_score vs churned (Yes/No)**.
* **Insight:** Customers with satisfaction < 6 show much higher churn likelihood.

---

## 🧱 How Your Module Could Work

1. **User loads dataset:**

   ```python
   df = pd.read_csv("retail_banking_customers.csv")
   ```

2. **Persona selected:**

   ```python
   persona = Persona.from_json("personas/retail_banking_cxo.json")
   ```

3. **Goal → Analysis mapping:**

   * If persona cares about churn → run churn analysis.
   * If persona cares about digital adoption → analyze app usage.

4. **Visualization output:**
   Generate tailored plots with titles and insights phrased in **persona’s preferred tone and detail level**.

---

✅ This way, the **same dataset** could be analyzed from different perspectives — e.g.,

* **Retail Banking CXO** cares about churn, adoption, and satisfaction.
* **Operations Manager in Banking** might instead care about transaction efficiency, fraud, and branch performance.

---

## Example How single Dataset can be interpreted differntly by different personas.

---

# 📊 Example Dataset: Customer Feedback (E-commerce Store)

Imagine we collect **customer survey data** with these fields:

| Customer\_ID | Rating (1–5) | Comment                                      | Order\_Value |
| ------------ | ------------ | -------------------------------------------- | ------------ |
| 101          | 2            | "Delivery was late and packaging was poor."  | \$120        |
| 102          | 5            | "Fast shipping, love the eco-friendly wrap!" | \$45         |
| 103          | 3            | "Product is okay, but too expensive."        | \$200        |
| 104          | 1            | "Terrible support, never buying again."      | \$80         |
| 105          | 4            | "Good quality, but shipping costs too high." | \$150        |

---

# 🎯 How Personas Interpret It

### 1. **Eco-Conscious Shopper (Customer Persona)**

* **Lens:** cares about sustainability, ethical sourcing, transparency.
* **Insights they would care about:**

  * Positive: Customer #102 praised eco-friendly packaging → ✅ shows alignment with eco-values.
  * Risk: Complaints about packaging quality (#101) → 🚨 could look like greenwashing if packaging is eco but not durable.
* **Output style:** trustworthy, medium detail → “Most customers are happy with eco-friendly packaging, but some still question quality.”

---

### 2. **Busy Product Manager (Mid-Level, SaaS Equivalent but here Retail)**

* **Lens:** cares about prioritizing improvements, roadmap decisions.
* **Insights they would care about:**

  * High pain points: Delivery delays (#101), support failures (#104), shipping costs (#105).
  * Feature request (implicit): Cheaper shipping options.
  * Prioritization: Fixing delivery + support would address 2 of 5 complaints (40%).
* **Output style:** concise, low detail → “Top 2 blockers: delivery reliability and support experience. Prioritize before new features.”

---

### 3. **CFO / Small Business Owner (Decision Maker)**

* **Lens:** cares about profit, retention, cost vs. benefit.
* **Insights they would care about:**

  * Lost revenue risk: Customer #104 (Order \$80) churned.
  * High-value risk: Customer #103 (\$200 order) felt product overpriced → potential churn from big spenders.
  * Positive: Customer #102 was delighted but low-value (\$45 order).
* **Output style:** practical, medium detail → “High-value customers complain about price and support; losing them impacts revenue more than shipping cost complaints.”

---

# 🧭 Takeaway

* **Same dataset** (5 rows of survey feedback).
* But through **different personas**:

  * **Eco-Conscious Shopper** sees it as a trust/values issue (greenwashing risk).
  * **Product Manager** sees it as a prioritization problem (fix shipping + support).
  * **CFO** sees it as a revenue retention problem (high-value churn risk).

👉 That’s exactly what **mindscope’s persona system** does:
It doesn’t change the data — it changes the **interpretation and prioritization** of that data depending on *who* the insights are for.
