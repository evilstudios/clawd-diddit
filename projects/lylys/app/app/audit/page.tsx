'use client';

import { useState } from 'react';
import Link from 'next/link';

export default function AuditPage() {
  const [youtubeUrl, setYoutubeUrl] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      // Extract channel ID from URL
      const channelId = extractChannelId(youtubeUrl);
      
      if (!channelId) {
        throw new Error('Invalid YouTube URL. Please enter a valid channel URL.');
      }

      // Call API to analyze channel
      const response = await fetch('/api/audit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ channelId, email }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.error || 'Failed to analyze channel');
      }

      const data = await response.json();
      
      // Redirect to results with audit ID
      window.location.href = `/audit/${data.auditId}`;
      
    } catch (err: any) {
      setError(err.message);
      setLoading(false);
    }
  };

  const extractChannelId = (url: string): string | null => {
    // Handle different YouTube URL formats
    const patterns = [
      /youtube\.com\/channel\/([^\/\?]+)/,
      /youtube\.com\/c\/([^\/\?]+)/,
      /youtube\.com\/@([^\/\?]+)/,
      /youtube\.com\/user\/([^\/\?]+)/,
    ];

    for (const pattern of patterns) {
      const match = url.match(pattern);
      if (match) return match[1];
    }

    // If it's just the channel ID
    if (url.match(/^[A-Za-z0-9_-]{24}$/)) {
      return url;
    }

    return null;
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-paper-white to-white">
      {/* Header */}
      <header className="container mx-auto px-4 py-6">
        <Link href="/" className="text-2xl font-bold text-heartbeat-red">
          LYLYS
        </Link>
      </header>

      {/* Main Content */}
      <section className="container mx-auto px-4 py-12 md:py-20">
        <div className="max-w-2xl mx-auto">
          {/* Title */}
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-bold text-studio-slate mb-4">
              Get Your Free <span className="text-heartbeat-red">Fan Audit</span>
            </h1>
            <p className="text-xl text-studio-slate/70">
              Discover who your top 1% superfans are in under 60 seconds
            </p>
          </div>

          {/* Form Card */}
          <div className="card">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* YouTube URL Input */}
              <div>
                <label htmlFor="youtube-url" className="block text-sm font-semibold text-studio-slate mb-2">
                  Your YouTube Channel URL
                </label>
                <input
                  id="youtube-url"
                  type="text"
                  value={youtubeUrl}
                  onChange={(e) => setYoutubeUrl(e.target.value)}
                  placeholder="https://youtube.com/@yourchannel"
                  className="w-full px-4 py-3 border-2 border-studio-slate/20 rounded-lg focus:border-connection-teal focus:outline-none transition-colors"
                  required
                  disabled={loading}
                />
                <p className="mt-2 text-xs text-studio-slate/60">
                  We'll analyze your last 5 videos to find your superfans
                </p>
              </div>

              {/* Email Input */}
              <div>
                <label htmlFor="email" className="block text-sm font-semibold text-studio-slate mb-2">
                  Your Email
                </label>
                <input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="your@email.com"
                  className="w-full px-4 py-3 border-2 border-studio-slate/20 rounded-lg focus:border-connection-teal focus:outline-none transition-colors"
                  required
                  disabled={loading}
                />
                <p className="mt-2 text-xs text-studio-slate/60">
                  We'll send your full report here (no spam, promise)
                </p>
              </div>

              {/* Error Message */}
              {error && (
                <div className="bg-heartbeat-red/10 border-2 border-heartbeat-red/30 rounded-lg p-4">
                  <p className="text-heartbeat-red text-sm font-medium">{error}</p>
                </div>
              )}

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className="btn-primary w-full text-lg disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <span className="flex items-center justify-center">
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Analyzing Your Channel...
                  </span>
                ) : (
                  'Analyze My Fans →'
                )}
              </button>

              {/* Privacy Note */}
              <p className="text-xs text-center text-studio-slate/60">
                By submitting, you agree to our{' '}
                <Link href="/privacy" className="underline">Privacy Policy</Link>
                {' '}and{' '}
                <Link href="/terms" className="underline">Terms of Service</Link>
              </p>
            </form>
          </div>

          {/* What You'll Get */}
          <div className="mt-12 grid md:grid-cols-3 gap-6 text-center">
            <div>
              <div className="text-4xl mb-2">🔍</div>
              <h3 className="font-semibold text-studio-slate mb-1">Superfan List</h3>
              <p className="text-sm text-studio-slate/70">
                See exactly who engages most
              </p>
            </div>
            <div>
              <div className="text-4xl mb-2">📊</div>
              <h3 className="font-semibold text-studio-slate mb-1">Engagement Score</h3>
              <p className="text-sm text-studio-slate/70">
                Quantify loyalty per fan
              </p>
            </div>
            <div>
              <div className="text-4xl mb-2">💡</div>
              <h3 className="font-semibold text-studio-slate mb-1">Recommendations</h3>
              <p className="text-sm text-studio-slate/70">
                How to reward them
              </p>
            </div>
          </div>

          {/* Trust Signals */}
          <div className="mt-8 text-center">
            <p className="text-sm text-studio-slate/60">
              ✓ No credit card required · ✓ Results in ~60 seconds · ✓ 100% free
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}
