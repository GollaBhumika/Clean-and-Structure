# Mint Technologies | Retail Sales Data Analytics

A data analytics project focused on cleaning retail sales data and extracting business insights using Python and SQL.

## Milestone 01: Data Cleaning & Preprocessing

### Objective
Clean and structure raw retail sales data to improve data quality and prepare it for analysis.

### Tools Used
- Python
- Pandas
- NumPy
- Jupyter Notebook

### Key Tasks
- Checked and handled duplicate and missing values.
- Standardized data and corrected data types.
- Investigated business anomalies and validated the cleaned dataset.
- Exported the cleaned data for further analysis.

**Notebook:** `notebooks/01_clean_and_structure.ipynb`

## Milestone 02: SQL Aggregations

### Objective
Load the cleaned dataset into SQLite and use SQL queries to identify meaningful business insights.

### Tools Used
- Python
- Pandas
- SQLite
- SQL
- Jupyter Notebook

### Key Tasks
- Loaded the cleaned dataset into a SQLite database.
- Performed five SQL aggregation queries.
- Analyzed sales trends and business performance using `GROUP BY`, `SUM()`, `AVG()`, and `ORDER BY`.
- Displayed query results using Pandas.

**Notebook:** `notebooks/02_sql_analysis.ipynb`

## Project Outcome

Developed a structured data analytics workflow covering data cleaning, preprocessing, SQL querying, and business insight generation.

## Milestone 03: Data Visualization

### Project Overview
This milestone focuses on transforming SQL analysis results and retail sales data into clear, professional visualizations to communicate business insights effectively.

### Objectives
- Visualize top-selling products and monthly sales trends.
- Compare sales performance across regions, customer segments, and product categories.
- Analyze the distribution of individual sales values.
- Explore variations in sales transactions and category contributions.

### Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
- SQLite

### Visualizations Created
1. Top 10 Products by Sales — Bar Chart
2. Monthly Sales Trend — Line Chart
3. Sales by Region — Bar Chart
4. Average Order Value by Customer Segment — Bar Chart
5. Sales by Product Category — Bar Chart
6. Distribution of Sales — Histogram
7. Sales Across Dataset Records — Scatter Plot
8. Sales Contribution by Category — Pie Chart, when suitable

### Key Outcomes
- Presented sales data through readable charts with titles and labels.
- Explored sales trends and differences across business categories.
- Added business takeaways to support data-driven interpretation.

### Deliverable
`notebooks/03_visualizations.ipynb`

### Conclusion
This milestone demonstrates how data visualization techniques can turn retail sales data into accessible visual insights and support business analysis and decision-making.

## Milestone 04: Deeper Analysis — RFM Customer Segmentation

### Project Overview
This milestone applies RFM analysis to retail sales data to evaluate customer purchasing behavior and identify customer segments based on recency, frequency, and monetary value.

### Objectives
- Calculate RFM metrics for each customer.
- Assign scores and create rule-based customer segments.
- Visualize customer distribution and purchasing behavior.
- Translate analytical results into potential business actions.

### Tools & Technologies
Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook.

### Key Deliverables
- RFM customer metrics and scores.
- Customer segmentation results.
- Customer segment distribution chart.
- Frequency versus monetary value scatter plot.
- Exported customer segmentation dataset.

### Notebook
`notebooks/04_deeper_analysis.ipynb`

### Business Impact
RFM analysis helps identify high-value and less-active customers, providing insights that can guide customer retention, loyalty programs, and re-engagement strategies.


## Milestone 05: Capstone — Streamlit Dashboard

### Project Overview

This milestone focuses on building an interactive retail sales dashboard using Streamlit to present business insights through KPI metrics, visualizations, and interactive filters.

### Objectives

- Develop an interactive web dashboard for retail sales analysis.
- Display key performance indicators (KPIs) using Streamlit metric cards.
- Present sales trends and performance through interactive charts.
- Enable users to explore sales data using sidebar filters.
- Summarize key findings and provide business recommendations.

### Tools & Technologies

- Python
- Pandas
- Streamlit
- Plotly
- Jupyter Notebook
- GitHub

### Dashboard Features

1. **Executive Summary** — Overview of retail sales performance using KPI metrics.
2. **Key Findings** — Insights from category-wise, region-wise, and monthly sales analysis.
3. **Recommendations** — Suggested business actions based on sales insights.
4. **Interactive Filters** — Filter sales data by region and product category.
5. **Sales Visualizations** — Charts for category sales, regional performance, monthly trends, and top 10 products.
6. **Dataset Preview** — View filtered retail sales records.

### Key Deliverables

- Interactive Streamlit dashboard.
- KPI cards and sales visualizations.
- Sidebar filters for data exploration.
- Business findings and recommendations.
- `app.py` — Dashboard application.
- `requirements.txt` — Required Python packages.

### How to Run the Dashboard

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the dashboard.

### Business Impact

The dashboard helps business stakeholders explore retail sales performance, identify top-selling products, compare regional and category-wise sales, and understand monthly sales trends to support data-driven decision-making.

### Deliverable

`app.py`

### Conclusion

This milestone demonstrates how Streamlit and interactive data visualizations can transform retail sales analysis into an accessible dashboard for business reporting and decision-making.

## Organization

**Mint Technologies** | Data Analytics Project




