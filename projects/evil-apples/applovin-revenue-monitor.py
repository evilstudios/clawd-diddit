#!/usr/bin/env python3
"""
Evil Apples - AppLovin Revenue Monitor
Pulls daily revenue metrics and alerts on anomalies
"""

import requests
import json
from datetime import datetime, timedelta
import os
from pathlib import Path

# AppLovin API Configuration
APPLOVIN_REPORT_KEY = "wrcTE_XOyy867Oz8VTTdq-gzZv125IF3d0LfcC4s40Zus5ZvxmaONF0JlJlc29mqHv9N0Rp3QwCLewL-_uTC4A"
APPLOVIN_API_BASE = "https://r.applovin.com/report"

# File paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "revenue-data"
DATA_DIR.mkdir(exist_ok=True)

class AppLovinMonitor:
    def __init__(self):
        self.report_key = APPLOVIN_REPORT_KEY
        self.headers = {
            "Accept": "application/json"
        }
    
    def get_revenue_report(self, start_date, end_date):
        """
        Fetch revenue report from AppLovin
        
        API Endpoint: https://r.applovin.com/report
        Parameters:
        - api_key: Report Key
        - start: YYYY-MM-DD
        - end: YYYY-MM-DD
        - columns: revenue,estimated_revenue,impressions,ecpm
        - format: json
        """
        params = {
            "api_key": self.report_key,
            "start": start_date,
            "end": end_date,
            "columns": "revenue,impressions,ecpm",
            "format": "json",
            "filter_application": "all"  # Can be filtered to specific app if needed
        }
        
        try:
            response = requests.get(APPLOVIN_API_BASE, params=params, headers=self.headers, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ API Error: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def get_yesterday_revenue(self):
        """Get revenue for yesterday"""
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        return self.get_revenue_report(yesterday, yesterday)
    
    def get_last_7_days(self):
        """Get revenue for last 7 days"""
        end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        return self.get_revenue_report(start_date, end_date)
    
    def get_last_30_days(self):
        """Get revenue for last 30 days"""
        end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        return self.get_revenue_report(start_date, end_date)
    
    def save_daily_snapshot(self, data):
        """Save daily revenue snapshot"""
        if not data:
            return
        
        today = datetime.now().strftime("%Y-%m-%d")
        filepath = DATA_DIR / f"revenue-{today}.json"
        
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Saved snapshot: {filepath}")
    
    def analyze_revenue_trends(self, data):
        """Analyze revenue data and detect anomalies"""
        if not data or "results" not in data:
            return None
        
        results = data["results"]
        if not results:
            # Return empty state instead of None
            return {
                "period_days": 0,
                "total_revenue": 0,
                "avg_daily_revenue": 0,
                "latest_revenue": 0,
                "avg_impressions": 0,
                "latest_impressions": 0,
                "avg_ecpm": 0,
                "latest_ecpm": 0,
                "anomalies": [],
                "no_data": True
            }
        
        # Extract metrics
        revenues = [float(r.get("revenue", 0)) for r in results]
        impressions = [int(r.get("impressions", 0)) for r in results]
        ecpms = [float(r.get("ecpm", 0)) for r in results]
        
        if not revenues:
            return None
        
        avg_revenue = sum(revenues) / len(revenues)
        total_revenue = sum(revenues)
        avg_impressions = sum(impressions) / len(impressions) if impressions else 0
        avg_ecpm = sum(ecpms) / len(ecpms) if ecpms else 0
        
        # Latest day
        latest = results[-1]
        latest_revenue = float(latest.get("revenue", 0))
        latest_impressions = int(latest.get("impressions", 0))
        latest_ecpm = float(latest.get("ecpm", 0))
        
        # Detect anomalies
        anomalies = []
        
        # Revenue drop > 30%
        if avg_revenue > 0 and latest_revenue < avg_revenue * 0.7:
            anomalies.append({
                "type": "revenue_drop",
                "severity": "high",
                "message": f"Revenue dropped {((avg_revenue - latest_revenue) / avg_revenue * 100):.1f}% below average",
                "latest": latest_revenue,
                "average": avg_revenue
            })
        
        # Impression drop > 40%
        if avg_impressions > 0 and latest_impressions < avg_impressions * 0.6:
            anomalies.append({
                "type": "impression_drop",
                "severity": "medium",
                "message": f"Impressions dropped {((avg_impressions - latest_impressions) / avg_impressions * 100):.1f}% below average",
                "latest": latest_impressions,
                "average": avg_impressions
            })
        
        # eCPM drop > 25%
        if avg_ecpm > 0 and latest_ecpm < avg_ecpm * 0.75:
            anomalies.append({
                "type": "ecpm_drop",
                "severity": "medium",
                "message": f"eCPM dropped {((avg_ecpm - latest_ecpm) / avg_ecpm * 100):.1f}% below average",
                "latest": latest_ecpm,
                "average": avg_ecpm
            })
        
        return {
            "period_days": len(results),
            "total_revenue": total_revenue,
            "avg_daily_revenue": avg_revenue,
            "latest_revenue": latest_revenue,
            "avg_impressions": avg_impressions,
            "latest_impressions": latest_impressions,
            "avg_ecpm": avg_ecpm,
            "latest_ecpm": latest_ecpm,
            "anomalies": anomalies
        }
    
    def format_report(self, analysis):
        """Format analysis into readable report"""
        if not analysis:
            return "❌ No data available"
        
        report = []
        report.append("📊 Evil Apples - AppLovin Revenue Report")
        report.append("=" * 50)
        
        # Check if no data
        if analysis.get('no_data'):
            report.append("")
            report.append("ℹ️  No revenue data for the requested period")
            report.append("")
            report.append("Possible reasons:")
            report.append("- AppLovin monetization not yet active")
            report.append("- No impressions served in this date range")
            report.append("- App is still in testing/development phase")
            report.append("")
            report.append("💡 This is normal for apps not yet in production")
            return "\n".join(report)
        
        report.append(f"Period: Last {analysis['period_days']} days")
        report.append("")
        report.append(f"💰 Total Revenue: ${analysis['total_revenue']:.2f}")
        report.append(f"📈 Avg Daily Revenue: ${analysis['avg_daily_revenue']:.2f}")
        report.append(f"💵 Latest Day Revenue: ${analysis['latest_revenue']:.2f}")
        report.append("")
        report.append(f"👁️  Avg Impressions: {analysis['avg_impressions']:,.0f}")
        report.append(f"👁️  Latest Impressions: {analysis['latest_impressions']:,}")
        report.append("")
        report.append(f"💸 Avg eCPM: ${analysis['avg_ecpm']:.2f}")
        report.append(f"💸 Latest eCPM: ${analysis['latest_ecpm']:.2f}")
        
        if analysis['anomalies']:
            report.append("")
            report.append("⚠️  ANOMALIES DETECTED:")
            report.append("-" * 50)
            for anomaly in analysis['anomalies']:
                severity_emoji = "🔴" if anomaly['severity'] == 'high' else "🟡"
                report.append(f"{severity_emoji} {anomaly['message']}")
        else:
            report.append("")
            report.append("✅ No anomalies detected - all metrics healthy")
        
        return "\n".join(report)


def main():
    """Main execution"""
    print("🎮 Evil Apples - AppLovin Revenue Monitor")
    print("=" * 50)
    
    monitor = AppLovinMonitor()
    
    # Fetch last 7 days
    print("\n📡 Fetching revenue data...")
    data = monitor.get_last_7_days()
    
    if data:
        # Save snapshot
        monitor.save_daily_snapshot(data)
        
        # Analyze
        analysis = monitor.analyze_revenue_trends(data)
        
        if analysis:
            # Print report
            print("\n")
            print(monitor.format_report(analysis))
            
            # Return alert status (for heartbeat integration)
            if analysis['anomalies']:
                return 1  # Alert needed
            return 0  # All good
        else:
            print("❌ Unable to analyze data")
            return 2
    else:
        print("❌ Failed to fetch revenue data")
        print("\nℹ️  Possible issues:")
        print("- Report Key might be incorrect")
        print("- API endpoint may have changed")
        print("- Network connectivity issues")
        print("\n💡 Try accessing: https://dash.applovin.com/documentation/mediation/reporting-api")
        return 2


if __name__ == "__main__":
    exit(main())
