'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { use } from 'react';

interface Superfan {
  username: string;
  commentCount: number;
  engagementScore: number;
  lastSeen: string;
  actions: string[];
}

export default function AuditResultsPage({ params }: { params: Promise<{ auditId: string }> }) {
  const resolvedParams = use(params);
  const [loading, setLoading] = useState(true);
  const [superfans, setSuperfans] = useState<Superfan[]>([]);

  useEffect(() => {
    // Simulate loading audit results
    // TODO: Fetch from API/Supabase
    setTimeout(() => {
      setSuperfans([
        {
          username: 'Sarah M.',
          commentCount: 47,
          engagementScore: 95,
          lastSeen: '2 hours ago',
          actions: ['Commented on last 5 videos', 'Shared 3 videos', 'Early viewer']
        },
        {
          username: 'Mike T.',
          commentCount: 38,
          engagementScore: 89,
          lastSeen: '1 day ago',
          actions: ['Commented on last 4 videos', 'Liked every video', '1-year subscriber']
        },
        {
          username: 'Jessica L.',
          commentCount: 31,
          engagementScore: 82,
          lastSeen: '3 hours ago',
          actions: ['Consistent commenter', 'High engagement rate', 'Shares content']
        },
        {
          username: 'David R.',
          commentCount: 29,
          engagementScore: 78,
          lastSeen: '5 hours ago',
          actions: ['Commented on last 3 videos', 'Replies to other fans', 'Community builder']
        },
        {
          username: 'Emily K.',
          commentCount: 24,
          engagementScore: 74,
          lastSeen: '1 day ago',
          actions: ['Early viewer', 'Consistent engagement', 'Positive comments']
        },
      ]);
      setLoading(false);
    }, 1500);
  }, [resolvedParams.auditId]);

  if (loading) {
    return (
      <main className="min-h-screen bg-gradient-to-br from-paper-white to-white flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-16 w-16 border-4 border-connection-teal border-t-transparent mb-4"></div>
          <h2 className="text-2xl font-bold text-studio-slate">Analyzing Your Fans...</h2>
          <p className="text-studio-slate/70 mt-2">This usually takes 30-60 seconds</p>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-paper-white to-white">
      {/* Header */}
      <header className="container mx-auto px-4 py-6 border-b border-studio-slate/10">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-heartbeat-red">
            LYLYS
          </Link>
          <Link href="/signup?from=audit" className="btn-primary">
            Start Rewarding Them →
          </Link>
        </div>
      </header>

      {/* Results */}
      <section className="container mx-auto px-4 py-12">
        <div className="max-w-4xl mx-auto">
          {/* Title */}
          <div className="text-center mb-12">
            <div className="inline-block bg-broadcast-amber/20 text-broadcast-amber px-4 py-2 rounded-full text-sm font-semibold mb-4">
              ✓ Analysis Complete
            </div>
            <h1 className="text-4xl md:text-5xl font-bold text-studio-slate mb-4">
              Your Top <span className="text-heartbeat-red">{superfans.length} Superfans</span>
            </h1>
            <p className="text-xl text-studio-slate/70">
              These fans engage with <strong>every single video</strong>. They deserve recognition.
            </p>
          </div>

          {/* Stats Overview */}
          <div className="grid md:grid-cols-3 gap-6 mb-12">
            <div className="card text-center">
              <div className="text-4xl font-bold text-heartbeat-red mb-2">{superfans.length}</div>
              <div className="text-sm font-semibold text-studio-slate mb-1">Superfans Found</div>
              <div className="text-xs text-studio-slate/60">Top 1% of your audience</div>
            </div>
            <div className="card text-center">
              <div className="text-4xl font-bold text-broadcast-amber mb-2">247</div>
              <div className="text-sm font-semibold text-studio-slate mb-1">Total Comments</div>
              <div className="text-xs text-studio-slate/60">From these 12 fans alone</div>
            </div>
            <div className="card text-center">
              <div className="text-4xl font-bold text-connection-teal mb-2">5</div>
              <div className="text-sm font-semibold text-studio-slate mb-1">Videos Analyzed</div>
              <div className="text-xs text-studio-slate/60">Your most recent content</div>
            </div>
          </div>

          {/* Superfan List */}
          <div className="space-y-4 mb-12">
            <h2 className="text-2xl font-bold text-studio-slate mb-6">
              Meet Your Superfans
            </h2>
            
            {superfans.map((fan, index) => (
              <div key={index} className="card hover:shadow-glow transition-shadow">
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <div className="w-12 h-12 rounded-full bg-gradient-to-br from-heartbeat-red to-broadcast-amber flex items-center justify-center text-white font-bold text-lg">
                        {fan.username.charAt(0)}
                      </div>
                      <div>
                        <h3 className="font-semibold text-studio-slate">{fan.username}</h3>
                        <p className="text-sm text-studio-slate/60">Last seen: {fan.lastSeen}</p>
                      </div>
                    </div>
                    
                    <div className="ml-15 space-y-1">
                      {fan.actions.map((action, i) => (
                        <div key={i} className="flex items-center gap-2 text-sm text-studio-slate/70">
                          <span className="text-connection-teal">✓</span>
                          <span>{action}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                  
                  <div className="text-right">
                    <div className="text-3xl font-bold text-heartbeat-red mb-1">{fan.engagementScore}</div>
                    <div className="text-xs text-studio-slate/60 mb-2">Engagement Score</div>
                    <div className="text-sm text-studio-slate/70">{fan.commentCount} comments</div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* CTA Section */}
          <div className="card bg-gradient-to-br from-heartbeat-red to-broadcast-amber text-white text-center p-12">
            <h2 className="text-3xl font-bold mb-4">
              Ready to Reward Them?
            </h2>
            <p className="text-lg mb-6 opacity-90">
              LYLYS can automatically send thank-you gifts when fans hit milestones.
              <br />
              No more manual tracking. No more missed opportunities.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link href="/signup?from=audit" className="bg-white text-heartbeat-red px-8 py-4 rounded-lg font-bold hover:shadow-2xl hover:-translate-y-1 transition-all inline-block">
                Start Free Trial →
              </Link>
              <Link href="/pricing" className="bg-white/10 backdrop-blur text-white border-2 border-white px-8 py-4 rounded-lg font-bold hover:bg-white/20 transition-colors inline-block">
                View Pricing
              </Link>
            </div>
          </div>

          {/* What Happens Next */}
          <div className="mt-12 grid md:grid-cols-3 gap-6">
            <div className="text-center">
              <div className="text-4xl mb-3">1️⃣</div>
              <h3 className="font-semibold text-studio-slate mb-2">Connect Your Channel</h3>
              <p className="text-sm text-studio-slate/70">
                Link your YouTube account for automatic tracking
              </p>
            </div>
            <div className="text-center">
              <div className="text-4xl mb-3">2️⃣</div>
              <h3 className="font-semibold text-studio-slate mb-2">Set Milestones</h3>
              <p className="text-sm text-studio-slate/70">
                Choose what deserves a reward (10th comment, 1-year anniversary, etc.)
              </p>
            </div>
            <div className="text-center">
              <div className="text-4xl mb-3">3️⃣</div>
              <h3 className="font-semibold text-studio-slate mb-2">Automate Everything</h3>
              <p className="text-sm text-studio-slate/70">
                LYLYS handles the rest. Fans get rewarded. Loyalty grows.
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
