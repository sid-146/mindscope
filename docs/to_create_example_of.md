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
