# Omnichannel Marketing & Customer Analytics Dashboard
### Interactive Marketing Performance & Unit Economics Analytics

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![SQL](https://img.shields.io/badge/SQL-Relational_Data-4479A1?style=flat-square&logo=mysql&logoColor=white)](dax_measures.md)
[![Interactive UI](https://img.shields.io/badge/Visualization-Chart.js_&_Tailwind-38B2AC?style=flat-square)](dashboard_preview.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

An end-to-end data analytics project analyzing 180 days of multi-channel digital ad spend and 2,500 customer transactions across Kenyan consumer hubs.

The goal: **connect top-of-funnel acquisition spend (Meta, TikTok, Google Ads, Email) to actual downstream customer retention, basket values, and county-level revenue.**

---

## Dashboard Interface

### 1. Executive Summary & Acquisition Channel ROAS
![Executive KPI Scorecard](screenshots/dashboard_screenshot_1.png)

### 2. County Sales Distribution & Customer Segment Retention
![Regional County Revenue & Customer Segments](screenshots/dashboard_screenshot_2.png)

---

## The Business Problem

E-commerce and retail marketing teams often track campaign performance inside platform silos:
* Meta and TikTok report low Cost-per-Click (CPC), but rarely show whether those clicks convert into repeat buyers.
* Google Ads drives high intent, but at a steeper Customer Acquisition Cost (CAC).
* Merchandising and logistics teams lack visibility into which geographic corridors in Kenya drive the bulk of order volume.

This project unifies campaign spend and transaction logs into an integrated analytical data model with an interactive dashboard interface.

---

## Data Model & Schemas

The model links two core transactional tables:

1. **`campaign_performance.csv`** (548 records)
   * Tracks daily advertising spend, impressions, clicks, conversions, and attributed revenue across:
     * Meta Ads (Instagram & Facebook retargeting)
     * TikTok Ads (short-form video campaigns)
     * Google Ads (Search & Shopping)
     * Email sequences (retention & cart reactivation flows)

2. **`customer_orders.csv`** (2,500 records)
   * Transaction-level e-commerce data containing:
     * `Order_ID`, `Customer_ID`, `Order_Date`
     * `County` (Nairobi, Mombasa, Kiambu, Nakuru, Kisumu, Eldoret, Machakos, etc.)
     * `Product_Category` (Electronics, Produce/Grocery, Health, Apparel, Home)
     * `Order_Value_KES`, `Discount_KES`
     * `Customer_Segment` (High-Value Champions, Loyal Active, At-Risk Churn, Bargain Shoppers)
     * `Repeat_Customer` flag (Yes / No)

---

## Key Metrics & Analytical Calculations

| Metric | Formula / Logic | Result | Business Interpretation |
| :--- | :--- | :--- | :--- |
| **Total Revenue** | `SUM(Order_Value_KES)` | **KES 14.8M** | Total sales across 2,500 transactions (+14.2% MoM growth) |
| **Total Ad Spend** | `SUM(Spend_KES)` | **KES 3.2M** | Blended digital advertising spend over 6 months |
| **Blended ROAS** | `Total Revenue / Total Ad Spend` | **4.62x** | Healthy return (exceeds target baseline of 3.5x) |
| **Blended CAC** | `Total Ad Spend / Total Conversions` | **KES 485** | Average marketing spend required to acquire a customer |
| **Average Order Value (AOV)** | `Total Sales Revenue / Total Orders` | **KES 5,920** | Average checkout basket size |
| **Repeat Purchase Rate** | `Repeat Orders / Total Orders` | **58.4%** | Healthy retention signal across active buyers |

*(Note: In addition to the Python/HTML implementation, corresponding DAX formulas are documented in [dax_measures.md](dax_measures.md) for self-serve BI integration).*

---

## Core Findings & Recommendations

1. **Email Drives the Highest Margin (8.4x ROAS):**
   * Automated email sequences cost least to run but yield the highest revenue-to-spend ratio. Retention automations should be prioritized over pure cold acquisition.
2. **TikTok as a Volume Discovery Engine (3.4x ROAS):**
   * TikTok generated high impression counts at lower CPC, making it effective for top-of-funnel discovery, but required Meta retargeting or email capture to drive conversion.
3. **Kenya Geographic Concentration:**
   * **Nairobi** accounts for 45% (KES 6.65M) of total revenue, followed by Mombasa (KES 1.78M) and Kiambu (KES 1.49M). Delivery routes and stock allocation should prioritize this central-to-coast corridor.
4. **Pareto Distribution in Customer Cohorts:**
   * "High-Value Champions" represent 20% of the customer base but drive 42% (KES 6.2M) of total sales. Targeted loyalty perks for this tier will protect the company's core revenue base.

---

## Repository Structure

```
marketing-bi-dashboard/
├── campaign_performance.csv        # 180-day multi-channel marketing spend data
├── customer_orders.csv             # 2,500 customer transactions across Kenyan counties
├── dax_measures.md                 # Analytical calculation formulas & logic
├── dashboard_preview.html          # Interactive HTML5/Chart.js prototype
├── generate_bi_data.py             # Python ETL script used to generate the data
├── power_bi_and_tableau_guide.md   # Reference guide for importing into BI tools
└── screenshots/                    # Dashboard UI captures
```

---

## How to Explore

* **Interactive Browser Preview:** Double-click `dashboard_preview.html` to explore the interactive dashboard locally in your browser.
* **Data & Scripts:** Run `python generate_bi_data.py` to inspect the ETL data generation and schema relationships.
