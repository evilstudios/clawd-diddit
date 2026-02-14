import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Digital Warmth Palette
        'heartbeat-red': '#FF4B5C',
        'broadcast-amber': '#FFB347',
        'connection-teal': '#00CEC9',
        'studio-slate': '#2D3436',
        'paper-white': '#F9F9F9',
        
        // Semantic aliases
        primary: '#FF4B5C',
        secondary: '#FFB347',
        accent: '#00CEC9',
        neutral: '#2D3436',
        'bg-light': '#F9F9F9',
      },
      boxShadow: {
        'glow': '0 0 20px rgba(255, 179, 71, 0.3)',
        'glow-md': '0 0 30px rgba(255, 179, 71, 0.4)',
        'glow-lg': '0 0 40px rgba(255, 179, 71, 0.5)',
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'sans-serif'],
        display: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
    },
  },
  plugins: [],
};

export default config;
