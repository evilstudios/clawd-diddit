#!/usr/bin/env python3
"""
Business Dashboard - Unified metrics tracking across all products
Run daily to monitor business health and identify opportunities
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class BusinessDashboard:
    """Track metrics across all business properties"""
    
    def __init__(self):
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.metrics = {
            'evil_apples': {},
            'wellplate_ai': {},
            'afoodable_ai': {},
            'wine_monkey': {}
        }
        
    def fetch_evil_apples_metrics(self):
        """Fetch Evil Apples game metrics"""
        # TODO: Add App Store Connect API integration
        # TODO: Add Google Play Console API integration
        # TODO: Add in-app analytics API
        
        metrics = {
            'dau': None,  # Daily Active Users
            'mau': None,  # Monthly Active Users
            'downloads_ios': None,
            'downloads_android': None,
            'revenue_iap': None,  # In-app purchases
            'revenue_ads': None,
            'revenue_physical': None,  # Card game sales
            'retention_d1': None,
            'retention_d7': None,
            'retention_d30': None,
            'arpu': None,
        }
        
        self.metrics['evil_apples'] = metrics
        return metrics
    
    def fetch_wellplate_metrics(self):
        """Fetch WellPlate AI metrics"""
        # TODO: Add Google Analytics API
        # TODO: Add database queries for sign-ups
        # TODO: Add Stripe API for revenue
        
        metrics = {
            'visitors': None,
            'signups_free': None,
            'signups_paid': None,
            'mrr': None,
            'churn_rate': None,
            'conversion_rate': None,
            'cac': None,
            'ltv': None,
        }
        
        self.metrics['wellplate_ai'] = metrics
        return metrics
    
    def fetch_afoodable_metrics(self):
        """Fetch Afoodable AI metrics"""
        metrics = {
            'visitors': None,
            'signups_free': None,
            'signups_paid': None,
            'mrr': None,
            'churn_rate': None,
            'conversion_rate': None,
            'feature_usage': {},
        }
        
        self.metrics['afoodable_ai'] = metrics
        return metrics
    
    def fetch_wine_monkey_metrics(self):
        """Fetch Wine Monkey metrics"""
        metrics = {
            'active_servers': None,
            'active_users': None,
            'paid_users': None,
            'mrr': None,
            'interactions_daily': None,
        }
        
        self.metrics['wine_monkey'] = metrics
        return metrics
    
    def calculate_combined_metrics(self):
        """Calculate business-wide KPIs"""
        total_mrr = 0
        
        for product in ['wellplate_ai', 'afoodable_ai', 'wine_monkey']:
            mrr = self.metrics[product].get('mrr')
            if mrr:
                total_mrr += mrr
        
        # Add Evil Apples subscription revenue if available
        ea_revenue = self.metrics['evil_apples'].get('revenue_iap', 0) or 0
        
        return {
            'total_mrr': total_mrr,
            'evil_apples_revenue': ea_revenue,
            'total_revenue': total_mrr + ea_revenue,
            'target_mrr': 20000,  # $5K × 4 products
            'progress_percent': (total_mrr / 20000 * 100) if total_mrr else 0
        }
    
    def generate_report(self) -> str:
        """Generate HTML dashboard report"""
        combined = self.calculate_combined_metrics()
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Business Dashboard - {self.date}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 1200px;
            margin: 40px auto;
            padding: 20px;
            background: #0f0f0f;
            color: #fff;
        }}
        h1 {{ color: #00ff88; }}
        h2 {{ color: #00ccff; border-bottom: 2px solid #00ccff; padding-bottom: 10px; }}
        .summary {{
            background: #1a1a1a;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #00ff88;
        }}
        .metric {{
            display: inline-block;
            margin: 10px 20px 10px 0;
        }}
        .metric-label {{
            color: #888;
            font-size: 12px;
            text-transform: uppercase;
        }}
        .metric-value {{
            font-size: 24px;
            font-weight: bold;
            color: #00ff88;
        }}
        .product {{
            background: #1a1a1a;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
        }}
        .progress-bar {{
            width: 100%;
            height: 30px;
            background: #2a2a2a;
            border-radius: 15px;
            overflow: hidden;
            margin: 10px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #00ff88, #00ccff);
            transition: width 0.3s;
        }}
        .status {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
        }}
        .status-good {{ background: #00ff88; color: #000; }}
        .status-warning {{ background: #ffaa00; color: #000; }}
        .status-needs-data {{ background: #666; color: #fff; }}
    </style>
</head>
<body>
    <h1>📊 Business Dashboard</h1>
    <p>Generated: {self.date}</p>
    
    <div class="summary">
        <h2>🎯 Overall Progress</h2>
        <div class="metric">
            <div class="metric-label">Total MRR</div>
            <div class="metric-value">${combined['total_mrr']:,.2f}</div>
        </div>
        <div class="metric">
            <div class="metric-label">Target MRR</div>
            <div class="metric-value">${combined['target_mrr']:,.2f}</div>
        </div>
        <div class="metric">
            <div class="metric-label">Progress</div>
            <div class="metric-value">{combined['progress_percent']:.1f}%</div>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {min(combined['progress_percent'], 100)}%"></div>
        </div>
    </div>
    
    <div class="product">
        <h2>🍎 Evil Apples</h2>
        <span class="status status-needs-data">Needs API Integration</span>
        {self._format_product_metrics(self.metrics['evil_apples'])}
    </div>
    
    <div class="product">
        <h2>🥗 WellPlate AI</h2>
        <span class="status status-needs-data">Needs API Integration</span>
        <div class="metric">
            <div class="metric-label">MRR Target</div>
            <div class="metric-value">$5,000</div>
        </div>
        {self._format_product_metrics(self.metrics['wellplate_ai'])}
    </div>
    
    <div class="product">
        <h2>🍽️ Afoodable AI</h2>
        <span class="status status-needs-data">Needs API Integration</span>
        <div class="metric">
            <div class="metric-label">MRR Target</div>
            <div class="metric-value">$5,000</div>
        </div>
        {self._format_product_metrics(self.metrics['afoodable_ai'])}
    </div>
    
    <div class="product">
        <h2>🍷 Wine Monkey</h2>
        <span class="status status-needs-data">Needs API Integration</span>
        <div class="metric">
            <div class="metric-label">MRR Target</div>
            <div class="metric-value">$5,000</div>
        </div>
        {self._format_product_metrics(self.metrics['wine_monkey'])}
    </div>
    
    <div class="summary">
        <h2>📋 Next Actions</h2>
        <ul>
            <li>Set up API integrations for each product</li>
            <li>Configure analytics tracking</li>
            <li>Implement daily automated reports</li>
            <li>Set up alerts for metric anomalies</li>
        </ul>
    </div>
</body>
</html>"""
        
        return html
    
    def _format_product_metrics(self, metrics: Dict) -> str:
        """Format product metrics as HTML"""
        html = ""
        for key, value in metrics.items():
            if value is not None:
                html += f"""
                <div class="metric">
                    <div class="metric-label">{key.replace('_', ' ').title()}</div>
                    <div class="metric-value">{value}</div>
                </div>
                """
        return html if html else "<p>No data available yet</p>"
    
    def save_report(self, filepath: str):
        """Save HTML report to file"""
        report = self.generate_report()
        with open(filepath, 'w') as f:
            f.write(report)
        print(f"Dashboard saved to: {filepath}")
    
    def run(self):
        """Run full dashboard update"""
        print(f"Fetching business metrics for {self.date}...")
        
        self.fetch_evil_apples_metrics()
        self.fetch_wellplate_metrics()
        self.fetch_afoodable_metrics()
        self.fetch_wine_monkey_metrics()
        
        # Save to JSON for historical tracking
        output_dir = '/root/clawd/analytics/daily'
        os.makedirs(output_dir, exist_ok=True)
        
        json_path = f'{output_dir}/{self.date}.json'
        with open(json_path, 'w') as f:
            json.dump({
                'date': self.date,
                'metrics': self.metrics,
                'combined': self.calculate_combined_metrics()
            }, f, indent=2)
        
        # Generate HTML report
        html_path = f'{output_dir}/{self.date}.html'
        self.save_report(html_path)
        
        return html_path


if __name__ == '__main__':
    dashboard = BusinessDashboard()
    report_path = dashboard.run()
    print(f"\n✅ Dashboard generated: {report_path}")
    print("\n📊 Next steps:")
    print("  1. Add API credentials for each service")
    print("  2. Implement data fetching methods")
    print("  3. Set up cron job for daily execution")
