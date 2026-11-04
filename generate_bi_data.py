import csv
import random
from datetime import datetime, timedelta

random.seed(42)

# Generate Campaign Performance Data
start_date = datetime(2026, 1, 1)
campaigns = [
    ("Mega Sales Q1", "Meta (Instagram)", "Retargeting"),
    ("Brand Awareness Jan", "TikTok", "Youth Demographic (18-24)"),
    ("Google Search High Intent", "Google Ads", "In-Market Shoppers"),
    ("Loyalty Email Blast", "Email Sequence", "Past 90-Day Buyers"),
    ("Easter Promo Flash", "Meta (Facebook)", "Broad Interest"),
    ("TikTok Influencer Collab", "TikTok", "Creative Video Briefs"),
    ("New Customer Welcome Series", "Email Sequence", "New Subscribers"),
    ("Mid-Year Clearance Sale", "Meta (Instagram)", "Engaged Followers"),
    ("Google Shopping Performance Max", "Google Ads", "E-Commerce Intent"),
    ("Customer Reactivation Flow", "Email Sequence", "At-Risk Churn")
]

campaign_rows = []
for i in range(180): # 180 days (Jan to June 2026)
    curr_date = start_date + timedelta(days=i)
    # Pick 2-4 active campaigns per day
    active_camps = random.sample(campaigns, random.randint(2, 4))
    for camp_name, platform, audience in active_camps:
        if platform == "TikTok":
            spend = random.randint(1500, 6000)
            impressions = spend * random.randint(35, 60)
            clicks = int(impressions * random.uniform(0.02, 0.045)) # CTR 2-4.5%
            conversions = int(clicks * random.uniform(0.03, 0.07))
            rev_multiplier = random.uniform(2.8, 4.5)
        elif platform.startswith("Meta"):
            spend = random.randint(2000, 8000)
            impressions = spend * random.randint(25, 45)
            clicks = int(impressions * random.uniform(0.018, 0.038)) # CTR 1.8-3.8%
            conversions = int(clicks * random.uniform(0.04, 0.09))
            rev_multiplier = random.uniform(3.2, 5.2)
        elif platform == "Google Ads":
            spend = random.randint(2500, 7000)
            impressions = spend * random.randint(15, 30)
            clicks = int(impressions * random.uniform(0.035, 0.065)) # Higher intent CTR
            conversions = int(clicks * random.uniform(0.06, 0.12)) # Higher conversion
            rev_multiplier = random.uniform(3.5, 6.0)
        else: # Email
            spend = random.randint(300, 1000) # ESP cost / marginal spend
            impressions = random.randint(5000, 18000) # Opens / deliveries
            clicks = int(impressions * random.uniform(0.08, 0.16)) # High click-to-open
            conversions = int(clicks * random.uniform(0.05, 0.14))
            rev_multiplier = random.uniform(6.0, 12.0)
            
        revenue = int(spend * rev_multiplier)
        campaign_rows.append([
            curr_date.strftime("%Y-%m-%d"),
            camp_name,
            platform,
            audience,
            spend,
            impressions,
            clicks,
            conversions,
            revenue
        ])

with open("marketing-bi-dashboard/campaign_performance.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Campaign_Name", "Platform", "Target_Audience", "Spend_KES", "Impressions", "Clicks", "Conversions", "Revenue_KES"])
    writer.writerows(campaign_rows)

print(f"Generated {len(campaign_rows)} campaign performance rows.")

# Generate Customer Orders Data
counties = ["Nairobi", "Mombasa", "Kiambu", "Nakuru", "Kisumu", "Eldoret (Uasin Gishu)", "Machakos", "Kajiado", "Kilifi", "Nyeri"]
county_weights = [0.45, 0.12, 0.10, 0.08, 0.06, 0.05, 0.05, 0.04, 0.03, 0.02]
categories = ["Electronics & Accessories", "Fresh Produce & Groceries", "Health & Personal Care", "Home & Kitchen", "Apparel & Fashion"]
segments = ["High-Value Champions", "Loyal Active", "At-Risk Churn", "Occasional Bargain Shoppers"]
segment_weights = [0.20, 0.40, 0.18, 0.22]

order_rows = []
customer_pool = [f"CUST_{j:04d}" for j in range(1, 650)] # 650 customers

for order_id in range(1001, 3501): # 2500 transactions
    order_date = start_date + timedelta(days=random.randint(0, 179))
    cust_id = random.choice(customer_pool)
    county = random.choices(counties, weights=county_weights)[0]
    category = random.choice(categories)
    segment = random.choices(segments, weights=segment_weights)[0]
    
    if segment == "High-Value Champions":
        order_val = random.randint(4500, 18000)
        discount = random.randint(200, 1500)
        repeat = "Yes"
    elif segment == "Loyal Active":
        order_val = random.randint(2200, 7500)
        discount = random.randint(100, 600)
        repeat = "Yes"
    elif segment == "At-Risk Churn":
        order_val = random.randint(1800, 6000)
        discount = random.randint(0, 400)
        repeat = random.choice(["Yes", "No"])
    else:
        order_val = random.randint(900, 3200)
        discount = random.randint(150, 700)
        repeat = "No"
        
    source = random.choices(["Meta (Instagram)", "TikTok", "Google Ads", "Email Sequence", "Direct/Organic"], weights=[0.28, 0.22, 0.25, 0.15, 0.10])[0]
    
    order_rows.append([
        f"ORD_{order_id}",
        cust_id,
        order_date.strftime("%Y-%m-%d"),
        county,
        source,
        category,
        order_val,
        discount,
        segment,
        repeat
    ])

with open("marketing-bi-dashboard/customer_orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Order_ID", "Customer_ID", "Order_Date", "County", "Channel_Source", "Product_Category", "Order_Value_KES", "Discount_KES", "Customer_Segment", "Repeat_Customer"])
    writer.writerows(order_rows)

print(f"Generated {len(order_rows)} customer order rows.")

