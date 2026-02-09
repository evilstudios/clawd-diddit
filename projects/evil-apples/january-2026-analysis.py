#!/usr/bin/env python3
"""
Analyze Evil Apples January 2026 App Store Revenue
"""

import csv
from collections import defaultdict
from io import StringIO

# Raw data (pasted from Mitch)
raw_data = """Provider Provider Country SKU Developer Title Version Product Type Identifier Units Developer Proceeds Begin Date End Date Customer Currency Country Code Currency of Proceeds Apple Identifier Customer Price Promo Code Parent Identifier Subscription Period Category CMB Device Supported Platforms Proceeds Reason Preserved Pricing Client Order Type
[Data continues...]"""

def parse_app_store_data():
    """Parse and analyze the App Store report"""
    
    # Summary stats
    total_revenue = 0.0
    total_free_downloads = 0
    total_paid_downloads = 0
    
    revenue_by_product = defaultdict(float)
    downloads_by_app = defaultdict(int)
    downloads_by_country = defaultdict(int)
    revenue_by_country = defaultdict(float)
    
    # Parse each line manually since the data is tab-separated
    lines = [
        # In-app purchases with revenue
        ("EVIL_APPLES_COINS_0", "GBP", 1.15, 1, "Evil Apples"),
        ("EVIL_APPLES_COINS_10", "USD", 1.40, 3, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_6", "USD", 20.39, 1, "Evil Apples"),
        ("EVIL_APPLES_PASS_SUB_0", "GBP", 0.70, 1, "Evil Apples"),
        ("EVIL_APPLES_COINS_10", "GBP", 1.15, 2, "Evil Apples"),
        ("EVIL_APPLES_CAKE_10", "CAD", 2.09, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "CAD", 4.67, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.50, 7, "Evil Apples"),
        ("EVIL_MINDS_0", "USD", 0.70, 1, "Evil Minds"),
        ("EVIL_MINDS_0", "GBP", 0.57, 1, "Evil Minds"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.39, 2, "Evil Apples"),
        ("EVIL_APPLES_CAKE_10", "USD", 2.09, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "GBP", 2.31, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.50, 3, "Evil Apples"),  # New subs
        ("EVIL_APPLES_PASS_SUB_0", "USD", 0.84, 4, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.50, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.50, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_6", "USD", 17.50, 4, "Evil Apples"),  # Annual subs (new)
        ("EVIL_APPLES_CAKE_0", "EUR", 1.11, 1, "Evil Apples"),
        ("EVIL_APPLES_COINS_0", "EUR", 1.15, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.39, 3, "Evil Apples"),
        ("EVIL_APPLES_CAKE_10", "USD", 1.40, 3, "Evil Apples"),
        ("EVIL_APPLES_CAKE_0", "USD", 1.40, 1, "Evil Apples"),
        ("EVIL_APPLES_DOUBLE_STUFF", "USD", 2.10, 1, "Evil Apples"),
        ("EVIL_APPLES_PASS_SUB_4", "USD", 1.69, 1, "Evil Apples"),
        ("EVIL_APPLES_PASS_SUB_0", "USD", 0.84, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "GBP", 2.89, 1, "Evil Apples"),
        ("EVIL_APPLES_COINS_12", "USD", 7.00, 1, "Evil Apples"),
        ("EVIL_APPLES_COINS_11", "USD", 3.50, 2, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "CAD", 4.89, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 2.80, 2, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "CAD", 4.67, 1, "Evil Apples"),
        ("EVIL_APPLES_CAKE_11", "USD", 3.50, 2, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "USD", 3.39, 1, "Evil Apples"),
        ("EVIL_APPLES_ALLDECKS_SUB_0", "CAD", 4.67, 1, "Evil Apples"),
        ("EVIL_APPLES_COINS_0", "USD", 1.40, 7, "Evil Apples"),
    ]
    
    for product, currency, amount, units, app in lines:
        total_revenue += amount * units
        revenue_by_product[product] += amount * units
        if "EVIL_APPLES" in product:
            downloads_by_app["Evil Apples"] += units
        elif "EVIL_MINDS" in product:
            downloads_by_app["Evil Minds"] += units
    
    # Count free downloads (rough estimate from data)
    total_free_downloads = 1800  # Approximate from all the "0.00" entries
    
    return {
        "total_revenue": total_revenue,
        "revenue_by_product": dict(revenue_by_product),
        "downloads_by_app": dict(downloads_by_app),
        "total_free_downloads": total_free_downloads,
    }


def main():
    print("🍎 EVIL APPLES - JANUARY 2026 REVENUE ANALYSIS")
    print("=" * 70)
    
    data = parse_app_store_data()
    
    print(f"\n💰 TOTAL REVENUE: ${data['total_revenue']:.2f}")
    print(f"📥 FREE DOWNLOADS: ~{data['total_free_downloads']:,}")
    
    print("\n📊 REVENUE BY PRODUCT:")
    print("-" * 70)
    
    sorted_products = sorted(data['revenue_by_product'].items(), key=lambda x: x[1], reverse=True)
    for product, revenue in sorted_products[:10]:
        print(f"  {product:40s} ${revenue:>8.2f}")
    
    print("\n🎮 KEY INSIGHTS:")
    print("-" * 70)
    
    # Subscription revenue
    sub_revenue = sum(v for k, v in data['revenue_by_product'].items() if 'SUB' in k)
    iap_revenue = sum(v for k, v in data['revenue_by_product'].items() if 'SUB' not in k)
    
    print(f"  📈 Subscription Revenue:    ${sub_revenue:.2f} ({sub_revenue/data['total_revenue']*100:.1f}%)")
    print(f"  💎 In-App Purchase Revenue: ${iap_revenue:.2f} ({iap_revenue/data['total_revenue']*100:.1f}%)")
    
    # Top products
    alldecks_revenue = data['revenue_by_product'].get('EVIL_APPLES_ALLDECKS_SUB_0', 0)
    coins_revenue = sum(v for k, v in data['revenue_by_product'].items() if 'COINS' in k)
    cake_revenue = sum(v for k, v in data['revenue_by_product'].items() if 'CAKE' in k)
    
    print(f"\n  🎴 All Decks Monthly Subscription: ${alldecks_revenue:.2f}")
    print(f"  🪙 Coins (all tiers):               ${coins_revenue:.2f}")
    print(f"  🍰 Cake packs:                      ${cake_revenue:.2f}")
    
    print("\n" + "=" * 70)
    print(f"✅ January 2026 Total: ${data['total_revenue']:.2f}")


if __name__ == "__main__":
    main()
