# Step-by-Step BI Dashboard Build Guide: Power BI & Tableau

This guide walks you through building an Executive Marketing & Customer Analytics Dashboard in either **Power BI Desktop** (Free) or **Tableau Public** (Free) in ~25 minutes.

---

## Architecture & Visual Hierarchy (3-Tier Layout)

```
+-----------------------------------------------------------------------------------+
| HEADER: Omnichannel Marketing & Customer Lifetime Analytics Dashboard             |
| Slicers: [Date Range]  [Channel / Platform]  [County]  [Customer Segment]         |
+-----------------------------------------------------------------------------------+
| ROW 1: EXECUTIVE KPI SUMMARY CARDS                                               |
| [ Total Revenue ]  | [ Ad Spend ]  | [ Blended ROAS ]  | [ CAC / CPA ]  | [ AOV ] |
+-----------------------------------------------------------------------------------+
| ROW 2: MARKETING ACQUISITION & ATTRIBUTION                                        |
| [ Left: Channel ROAS & Spend ]        | [ Right: Monthly Revenue & Spend Trend ]  |
| (Clustered Bar / Combo Chart)         | (Line & Area Chart)                       |
+-----------------------------------------------------------------------------------+
| ROW 3: CUSTOMER SEGMENTS & REGIONAL GEOGRAPHY                                     |
| [ Left: Revenue by Kenyan County ]    | [ Right: Customer Segment Distribution ]  |
| (Filled Map / Ranked Horizontal Bar)  | (Donut Chart / Treemap with Churn Risk)   |
+-----------------------------------------------------------------------------------+
```

---

## Option A: Building in Power BI Desktop (Recommended)

### Step 1: Ingest the Datasets
1. Open Power BI Desktop.
2. Click **Get Data** -> **Text/CSV**.
3. Load `campaign_performance.csv` and `customer_orders.csv`.
4. In **Power Query Editor**, ensure:
   * Dates are formatted as `Date`.
   * Numerical columns (`Spend_KES`, `Revenue_KES`, `Order_Value_KES`) are formatted as `Decimal Number` or `Fixed Decimal Number`.
5. Click **Close & Apply**.

### Step 2: Establish the Data Model
* Go to the **Model View** (left pane icon).
* Create a dedicated Date table or link `campaign_performance[Date]` and `customer_orders[Order_Date]` via an active Date Dimension or shared Platform/Channel key if comparing cross-attribution.

### Step 3: Create Measures Table
* On the **Home** tab, click **Enter Data**, name the table `_Measures`.
* Right-click `_Measures` -> **New Measure** and paste the formulas from `dax_measures.md` (e.g., `Total Ad Spend`, `Total Revenue`, `Blended ROAS`, `CAC`, `AOV`).

### Step 4: Assemble the Visuals
1. **Top Cards (Multi-Row Card or New Card Visual):**
   * Fields: `[Total Sales Revenue]`, `[Total Ad Spend]`, `[Blended ROAS]`, `[CAC]`, `[AOV]`.
2. **Channel Performance (Clustered Column Chart):**
   * X-axis: `campaign_performance[Platform]`
   * Y-axis: `[Total Attributed Revenue]`, `[Total Ad Spend]`
   * Line Y-axis: `[Blended ROAS]`
3. **Geographic Revenue (Bar Chart or Azure Map):**
   * Y-axis: `customer_orders[County]`
   * X-axis: `[Total Sales Revenue]` (Sort descending by revenue).
4. **Customer Segments (Donut Chart / Matrix):**
   * Legend: `customer_orders[Customer_Segment]`
   * Values: `[Total Sales Revenue]` and Count of `Customer_ID`.
5. **Interactive Filters (Slicers):**
   * Add slicers for `Date`, `Platform`, and `Customer_Segment`.

### Step 5: Save & Publish
* Save as `Omnichannel_Marketing_Analytics.pbix`.
* (Optional) Click **Publish** to publish to your free Power BI Service workspace, or export a 1-page PDF / high-res screenshots for GitHub!

---

## Option B: Building in Tableau Public (Free)

1. Open **Tableau Public** (free download from `public.tableau.com`).
2. Click **Text file** -> select `campaign_performance.csv`. Add `customer_orders.csv` as a second connection.
3. Build 4 Worksheets:
   * **Sheet 1: KPI Cards** (Measure Values formatted cleanly).
   * **Sheet 2: Spend vs. Revenue by Platform** (Platform on Columns, Spend & Revenue on Rows with dual-axis).
   * **Sheet 3: Regional Kenya County Sales** (County on Rows, SUM(Order Value) on Columns, sorted).
   * **Sheet 4: Customer Segmentation & Churn** (Customer Segment on Rows, Repeat Customer on Color).
4. Create a **New Dashboard**:
   * Set size to **Automatic** or **Fixed (1920 x 1080)**.
   * Drag your 4 sheets into the layout container.
   * Add interactive filter controls for Platform and Date.
5. Click **Server** -> **Tableau Public** -> **Save to Tableau Public As...**.
6. You instantly receive a live, interactive URL that anyone in the world can view and click on!

