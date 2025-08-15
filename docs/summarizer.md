# **Summarizer**

The **Summarizer** component is responsible for generating descriptive metadata for a given dataset.
It works in two stages:

1. **Local Summary Generation** – Uses statistical and structural analysis to produce column-level and dataset-level summaries without using generative models.
2. **LLM Summary Enrichment** – Enhances the locally generated summary using a Large Language Model (LLM) to produce a concise, human-readable 1–2 liner description.

---

## **Overview**

-   **Input**: Dataset in the form of a Polars DataFrame.
-   **Output**:

    -   Local summary in JSON format (currently; will migrate to Pydantic models in the future).
    -   Enhanced summary using an LLM.

-   **Process**:

    1. Analyze each column to determine its type and compute relevant metrics.
    2. Generate dataset-level statistics and metadata.
    3. Feed local summary into LLM with a predefined prompt to produce an enriched natural language description.

---

## **Initialization**

-   **Input Source**: Receives data from the **Manager** module.
-   **Initialization**: The Manager instantiates a `Summarizer` object and passes the DataFrame.
-   **Scope**: Works at **column-level** first, then aggregates to produce dataset-level insights.

---

## **Local Summary**

The local summary process is purely statistical/structural, without AI-generated text.
It includes:

### 1. **Datatype Identification**

For each column:

-   Use Polars' schema inspection (`df.schema`) to determine the declared datatype.
-   Map to high-level categories:

    -   **Numeric** (integer, float)
    -   **Categorical** (string with low unique count)
    -   **Datetime** (date/time types)
    -   **Object** (complex structures: lists, dictionaries, JSON strings)

---

### 2. **Numeric Columns Analysis**

For numeric columns, compute:

| Metric             | Formula                                                    | Description                        |
| ------------------ | ---------------------------------------------------------- | ---------------------------------- |
| Mean               | $\bar{x} = \frac{\sum_{i=1}^n x_i}{n}$                     | Average value                      |
| Median             | Middle value after sorting                                 | Robust measure of central tendency |
| Minimum            | $\min(x)$                                                  | Lowest value                       |
| Maximum            | $\max(x)$                                                  | Highest value                      |
| Standard Deviation | $\sigma = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n}}$ | Spread of values                   |
| Sample Values      | Random selection from column                               | Gives a sense of actual values     |

**Example Output**:

```json
{
    "column_name": "age",
    "type": "numeric",
    "mean": 35.4,
    "median": 34,
    "min": 18,
    "max": 65,
    "std_dev": 8.9,
    "samples": [22, 45, 33]
}
```

---

### 3. **Categorical Identification**

-   **Heuristic**:
    A column is considered _categorical_ if:

    -   Datatype is string, **and**
    -   Unique values count ≤ 20% of total rows (threshold adjustable), **and**
    -   Values repeat frequently.

-   **Metadata to capture**:

    -   Unique values count
    -   Top N most frequent categories with their counts and percentages
    -   Mode (most frequent category)

**Example Output**:

```json
{
    "column_name": "gender",
    "type": "categorical",
    "unique_count": 3,
    "top_values": [
        { "value": "Male", "count": 560, "percentage": 56.0 },
        { "value": "Female", "count": 430, "percentage": 43.0 },
        { "value": "Other", "count": 10, "percentage": 1.0 }
    ],
    "mode": "Male"
}
```

---

### 4. **Time Series Identification**

-   **Heuristic**:

    -   Datatype is date/datetime, **or**
    -   Values are strings that can be parsed into dates.

-   **Metadata to capture**:

    -   Minimum date
    -   Maximum date
    -   Frequency detection:

        -   Compute differences between consecutive sorted dates.
        -   If differences are constant → fixed frequency (e.g., daily, monthly).
        -   Use mode of time deltas to infer periodicity.

**Example Output**:

```json
{
    "column_name": "order_date",
    "type": "datetime",
    "min_date": "2023-01-01",
    "max_date": "2023-12-31",
    "inferred_frequency": "daily"
}
```

---

### 5. **Object Columns**

-   Capture metadata for stringified JSON, lists, or dictionaries.
-   Possible metrics:

    -   Structure type (list/dict)
    -   Avg. length or key count
    -   Common keys across rows (for dicts)

---

## **LLM Summary**

### **Purpose**

The LLM Summary converts raw statistical output into a concise, human-readable insight.

### **Process**:

1. Create a **prompt** combining:

    - Column name
    - Local summary JSON
    - Example phrasing instructions (e.g., _"Summarize in 1–2 lines focusing on meaning, trends, and anomalies"_)

2. Send prompt to LLM.
3. Receive and store natural language output.

### **Example Prompt to LLM**:

```plaintext
Given the following metadata for a column, generate a 1–2 line human-readable summary:

Column: age
Type: numeric
Mean: 35.4
Median: 34
Min: 18
Max: 65
Std Dev: 8.9
Samples: [22, 45, 33]

Focus on describing what the values represent, typical ranges, and any noticeable spread.
```

### **Example LLM Output**:

> "The 'age' column contains ages ranging from 18 to 65, with an average around 35 years, indicating a predominantly middle-aged population."

---

## **Dataset-Level Summary**

After processing all columns:

-   Aggregate column summaries to create an overall dataset description.
-   LLM prompt includes:

    -   Purpose of dataset (if provided)
    -   Column-level summaries
    -   Data coverage (row/column counts, date range if time-based)

**Example**:

> "The dataset consists of 1,000 records capturing customer demographics, purchase history, and transaction dates. Most customers are aged 25–45, with purchases recorded daily throughout 2023."

---

## **Final Output Structure**

```json
{
  "dataset_summary": {
    "row_count": 1000,
    "column_count": 12,
    "description": "Generated by LLM"
  },
  "columns": [
    {
      "name": "age",
      "local_summary": {...},
      "llm_summary": "..."
    },
    ...
  ]
}
```

## Diagram:

```mermaid
flowchart TD
    A[Manager Module] --> B[Initialize Summarizer with Polars DataFrame]
    B --> C[Local Summary Generation]
    
    %% Local Summary Steps
    C --> C1[Datatype Identification]
    C1 --> C2[Numeric Column Analysis:
    mean, median, min, max, std, samples]
    C1 --> C3[Categorical Identification:
    unique count, mode, top values]
    C1 --> C4[Time Series Identification:
    min/max date, frequency]
    C1 --> C5[Object Column Analysis:
    structure, key counts, common keys]
    
    %% Output of Local Summary
    C2 --> D[Local Summary JSON]
    C3 --> D
    C4 --> D
    C5 --> D
    
    %% LLM Summary
    D --> E[LLM Summary Enrichment]
    E --> E1[Create Prompt using Local Summary]
    E1 --> E2[Send Prompt to LLM]
    E2 --> E3[Receive 1–2 line human-readable description]
    
    %% Dataset Level
    E3 --> F[Aggregate Column Summaries for Dataset-Level Summary]
    
    %% Final Output
    F --> G[Final Output JSON:
    Local + LLM Summaries]

```