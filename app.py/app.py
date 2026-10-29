
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Dashboard")
st.markdown("Interactive analysis of retail sales data")

# Load cleaned dataset
DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "Data",
    "Cleaned data",
    "cleaned_dataset.csv"
)

df = pd.read_csv(DATA_FILE)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

regions = ["All"] + sorted(df["region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

# KPI cards
total_sales = filtered_df["sales"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_id"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Unique Orders", f"{total_orders:,}")
col3.metric("Unique Customers", f"{total_customers:,}")

st.divider()

# Sales by category
st.subheader("Sales by Category")

category_sales = (
    filtered_df.groupby("category", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)

fig_category = px.bar(
    category_sales,
    x="category",
    y="sales",
    color="category",
    title="Total Sales by Category"
)

st.plotly_chart(fig_category, use_container_width=True)

# Sales by region
st.subheader("Sales by Region")

region_sales = (
    filtered_df.groupby("region", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)

fig_region = px.bar(
    region_sales,
    x="region",
    y="sales",
    color="region",
    title="Total Sales by Region"
)

st.plotly_chart(fig_region, use_container_width=True)

# Monthly sales trend
st.subheader("Monthly Sales Trend")

date_df = filtered_df.dropna(subset=["order_date"]).copy()
date_df["Month"] = date_df["order_date"].dt.to_period("M").astype(str)

monthly_sales = (
    date_df.groupby("Month", as_index=False)["sales"]
    .sum()
    .sort_values("Month")
)

fig_monthly = px.line(
    monthly_sales,
    x="Month",
    y="sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig_monthly, use_container_width=True)

# Top 10 products
st.subheader("Top 10 Products by Sales")

top_products = (
    filtered_df.groupby("product_name", as_index=False)["sales"]
    .sum()
    .nlargest(10, "sales")
    .sort_values("sales", ascending=True)
)

fig_products = px.bar(
    top_products,
    x="sales",
    y="product_name",
    orientation="h",
    title="Top 10 Products"
)

st.plotly_chart(fig_products, use_container_width=True)

# Data preview
with st.expander("View Filtered Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

st.caption("Retail Sales Dashboard | Mint Technologies Project")
