import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LYLYS - Love Your Superfans",
  description: "Automate creator-to-fan gratitude. Track your top 1% and reward them automatically.",
  keywords: ["creator tools", "fan engagement", "YouTube creators", "loyalty platform"],
  openGraph: {
    title: "LYLYS - Stop Losing Your Superfans",
    description: "Automate gratitude. Build loyalty. Grow revenue.",
    url: "https://loveyouloveyourshow.com",
    siteName: "LYLYS",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "LYLYS - Love Your Superfans",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "LYLYS - Stop Losing Your Superfans",
    description: "Automate gratitude. Build loyalty. Grow revenue.",
    images: ["/og-image.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
