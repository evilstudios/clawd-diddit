import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-paper-white to-white">
      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20 md:py-32">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold text-studio-slate mb-6">
            Your <span className="text-heartbeat-red">Superfans</span> Are Leaving
          </h1>
          
          <p className="text-xl md:text-2xl text-studio-slate/80 mb-8 max-w-2xl mx-auto">
            Automate gratitude. Build loyalty. Grow revenue.
          </p>
          
          <p className="text-lg text-studio-slate/70 mb-12 max-w-2xl mx-auto">
            Mid-tier creators have 10-100K subscribers but lose touch with their most loyal fans.
            <strong> LYLYS tracks engagement and rewards your top 1% automatically.</strong>
          </p>
          
          <Link 
            href="/audit" 
            className="btn-primary inline-block text-lg"
          >
            Get Your Free Fan Audit →
          </Link>
          
          <p className="mt-4 text-sm text-studio-slate/60">
            No credit card required • See results in 60 seconds
          </p>
        </div>
      </section>

      {/* Features Grid */}
      <section className="container mx-auto px-4 py-16">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center text-studio-slate mb-16">
            How LYLYS Works
          </h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {/* Scout */}
            <div className="card">
              <div className="text-4xl mb-4">🔍</div>
              <h3 className="text-xl font-semibold text-studio-slate mb-3">
                Scout
              </h3>
              <p className="text-studio-slate/70">
                Automatically find your superfans who engage with every video, comment consistently, and drive real community growth.
              </p>
            </div>

            {/* SDR */}
            <div className="card">
              <div className="text-4xl mb-4">📊</div>
              <h3 className="text-xl font-semibold text-studio-slate mb-3">
                Analyze
              </h3>
              <p className="text-studio-slate/70">
                Get detailed Fan Audits showing who your top 1% are, what they engage with, and when they need recognition.
              </p>
            </div>

            {/* Concierge */}
            <div className="card">
              <div className="text-4xl mb-4">💌</div>
              <h3 className="text-xl font-semibold text-studio-slate mb-3">
                Track
              </h3>
              <p className="text-studio-slate/70">
                Monitor milestones like 10th comment, 1-year anniversary, or first donation. Never miss a moment to say thanks.
              </p>
            </div>

            {/* Fulfillment */}
            <div className="card">
              <div className="text-4xl mb-4">🎁</div>
              <h3 className="text-xl font-semibold text-studio-slate mb-3">
                Reward
              </h3>
              <p className="text-studio-slate/70">
                Ship physical thank-you gifts automatically. Stickers, hats, cards—all branded, all automated, all meaningful.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Social Proof */}
      <section className="container mx-auto px-4 py-16 bg-white/50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center text-studio-slate mb-12">
            Creators Love LYLYS
          </h2>
          
          <div className="grid md:grid-cols-2 gap-8">
            <div className="card border-l-4 border-heartbeat-red">
              <p className="text-studio-slate/80 mb-4 italic">
                "I had no idea I had 23 fans who watched every video. LYLYS found them and sent thank-you gifts automatically."
              </p>
              <p className="text-sm font-semibold text-studio-slate">
                — Sarah M., Podcast Creator
              </p>
              <p className="text-xs text-studio-slate/60">
                42K subscribers
              </p>
            </div>

            <div className="card border-l-4 border-broadcast-amber">
              <p className="text-studio-slate/80 mb-4 italic">
                "My engagement went up 40% after I started rewarding my top fans. LYLYS made it effortless."
              </p>
              <p className="text-sm font-semibold text-studio-slate">
                — Mike T., Gaming Channel
              </p>
              <p className="text-xs text-studio-slate/60">
                78K subscribers
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Preview */}
      <section className="container mx-auto px-4 py-16">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center text-studio-slate mb-4">
            Simple, Transparent Pricing
          </h2>
          <p className="text-center text-studio-slate/70 mb-12">
            Start free. Scale as you grow.
          </p>
          
          <div className="grid md:grid-cols-4 gap-6">
            {/* Free */}
            <div className="card text-center">
              <h3 className="text-2xl font-bold text-studio-slate mb-2">Free</h3>
              <p className="text-4xl font-bold text-heartbeat-red mb-4">$0</p>
              <ul className="text-left text-sm text-studio-slate/70 space-y-2 mb-6">
                <li>✓ 1 Fan Audit/month</li>
                <li>✓ Manual rewards</li>
                <li>✓ Email support</li>
              </ul>
              <Link href="/signup" className="btn-primary w-full block text-center">
                Start Free
              </Link>
            </div>

            {/* Starter */}
            <div className="card text-center border-2 border-connection-teal">
              <div className="inline-block bg-connection-teal text-white text-xs px-3 py-1 rounded-full mb-2">
                POPULAR
              </div>
              <h3 className="text-2xl font-bold text-studio-slate mb-2">Starter</h3>
              <p className="text-4xl font-bold text-heartbeat-red mb-4">$49</p>
              <ul className="text-left text-sm text-studio-slate/70 space-y-2 mb-6">
                <li>✓ Unlimited audits</li>
                <li>✓ 50 auto-rewards/mo</li>
                <li>✓ Email support</li>
              </ul>
              <Link href="/signup?plan=starter" className="btn-primary w-full block text-center">
                Get Started
              </Link>
            </div>

            {/* Pro */}
            <div className="card text-center">
              <h3 className="text-2xl font-bold text-studio-slate mb-2">Pro</h3>
              <p className="text-4xl font-bold text-heartbeat-red mb-4">$149</p>
              <ul className="text-left text-sm text-studio-slate/70 space-y-2 mb-6">
                <li>✓ Everything in Starter</li>
                <li>✓ 200 auto-rewards/mo</li>
                <li>✓ Custom designs</li>
                <li>✓ Priority support</li>
              </ul>
              <Link href="/signup?plan=pro" className="btn-primary w-full block text-center">
                Upgrade to Pro
              </Link>
            </div>

            {/* Enterprise */}
            <div className="card text-center bg-studio-slate text-white">
              <h3 className="text-2xl font-bold mb-2">Enterprise</h3>
              <p className="text-4xl font-bold text-broadcast-amber mb-4">$499</p>
              <ul className="text-left text-sm text-white/80 space-y-2 mb-6">
                <li>✓ Unlimited everything</li>
                <li>✓ White-label option</li>
                <li>✓ Dedicated manager</li>
                <li>✓ API access</li>
              </ul>
              <Link href="/contact" className="bg-broadcast-amber text-studio-slate px-6 py-3 rounded-lg font-semibold w-full block text-center hover:shadow-glow transition-shadow">
                Contact Sales
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="container mx-auto px-4 py-20">
        <div className="max-w-4xl mx-auto text-center bg-gradient-to-br from-heartbeat-red to-broadcast-amber text-white rounded-2xl p-12 shadow-glow-lg">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            Stop Losing Your Superfans
          </h2>
          <p className="text-xl mb-8 opacity-90">
            See exactly who your top 1% fans are in under 60 seconds
          </p>
          <Link href="/audit" className="bg-white text-heartbeat-red px-8 py-4 rounded-lg font-bold text-lg inline-block hover:shadow-2xl hover:-translate-y-1 transition-all">
            Get Your Free Fan Audit →
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-studio-slate text-white py-12">
        <div className="container mx-auto px-4">
          <div className="max-w-6xl mx-auto grid md:grid-cols-4 gap-8">
            <div>
              <h3 className="text-2xl font-bold text-heartbeat-red mb-4">LYLYS</h3>
              <p className="text-white/70 text-sm">
                Loyalty-as-a-Service for mid-tier creators
              </p>
            </div>
            
            <div>
              <h4 className="font-semibold mb-3">Product</h4>
              <ul className="space-y-2 text-sm text-white/70">
                <li><Link href="/features">Features</Link></li>
                <li><Link href="/pricing">Pricing</Link></li>
                <li><Link href="/audit">Free Audit</Link></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-3">Company</h4>
              <ul className="space-y-2 text-sm text-white/70">
                <li><Link href="/about">About</Link></li>
                <li><Link href="/blog">Blog</Link></li>
                <li><Link href="/contact">Contact</Link></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-3">Legal</h4>
              <ul className="space-y-2 text-sm text-white/70">
                <li><Link href="/privacy">Privacy</Link></li>
                <li><Link href="/terms">Terms</Link></li>
              </ul>
            </div>
          </div>
          
          <div className="max-w-6xl mx-auto mt-12 pt-8 border-t border-white/10 text-center text-white/60 text-sm">
            <p>© 2026 LoveYouLoveYourShow.com · Built with Digital Warmth 💝</p>
          </div>
        </div>
      </footer>
    </main>
  );
}
