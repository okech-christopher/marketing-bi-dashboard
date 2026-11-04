# Production DAX Measures for Power BI

These measures are organized by analytical category and are ready to copy directly into Power BI Desktop.

---

### 1. Financial & Executive Performance
```dax
// Total Marketing Spend
Total Ad Spend = SUM(campaign_performance[Spend_KES])

// Total Attributed Revenue
Total Attributed Revenue = SUM(campaign_performance[Revenue_KES])

// Total E-Commerce Sales Revenue
Total Sales Revenue = SUM(customer_orders[Order_Value_KES])

// Blended Return on Ad Spend (ROAS)
Blended ROAS = 
DIVIDE(
    [Total Attributed Revenue], 
    [Total Ad Spend], 
    0
)

// Gross Margin After Ad Spend (Contribution Margin)
Net Revenue Post-Ads = [Total Attributed Revenue] - [Total Ad Spend]
```

---

### 2. Digital Marketing Efficiency & Conversion Funnel
```dax
// Total Impressions
Total Impressions = SUM(campaign_performance[Impressions])

// Total Clicks
Total Clicks = SUM(campaign_performance[Clicks])

// Total Conversions
Total Conversions = SUM(campaign_performance[Conversions])

// Click-Through Rate (CTR)
Overall CTR = 
DIVIDE(
    [Total Clicks], 
    [Total Impressions], 
    0
)

// Cost Per Click (CPC)
Cost Per Click (CPC) = 
DIVIDE(
    [Total Ad Spend], 
    [Total Clicks], 
    0
)

// Customer Acquisition Cost (CAC / CPA)
Cost Per Acquisition (CAC) = 
DIVIDE(
    [Total Ad Spend], 
    [Total Conversions], 
    0
)

// Conversion Rate (CVR)
Conversion Rate = 
DIVIDE(
    [Total Conversions], 
    [Total Clicks], 
    0
)
```

---

### 3. Customer Lifetime & Basket Analytics
```dax
// Total Unique Customers
Total Customers = DISTINCTCOUNT(customer_orders[Customer_ID])

// Total Orders Placed
Total Orders = COUNTROWS(customer_orders)

// Average Order Value (AOV)
Average Order Value (AOV) = 
DIVIDE(
    [Total Sales Revenue], 
    [Total Orders], 
    0
)

// Repeat Customer Rate
Repeat Orders Count = 
CALCULATE(
    COUNTROWS(customer_orders), 
    customer_orders[Repeat_Customer] = "Yes"
)

Repeat Order Percentage = 
DIVIDE(
    [Repeat Orders Count], 
    [Total Orders], 
    0
)

// Revenue from High-Value Champions
Champion Segment Revenue = 
CALCULATE(
    [Total Sales Revenue], 
    customer_orders[Customer_Segment] = "High-Value Champions"
)
```

---

### 4. Time Intelligence & MoM Trends
```dax
// Monthly Spend
Monthly Spend = 
CALCULATE(
    [Total Ad Spend], 
    DATESMTD(campaign_performance[Date])
)

// Prior Month Revenue
Prior Month Revenue = 
CALCULATE(
    [Total Sales Revenue], 
    DATEADD(customer_orders[Order_Date], -1, MONTH)
)

// MoM Revenue Growth %
MoM Revenue Growth % = 
DIVIDE(
    [Total Sales Revenue] - [Prior Month Revenue], 
    [Prior Month Revenue], 
    0
)
```

