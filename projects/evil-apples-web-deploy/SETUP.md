# Evil Apples Web Version - Setup & Deployment

## Current Status

✅ **Frontend:** React app built and running on port 3001
✅ **Components:** LoginScreen, GameLobby, GameRoom, Cards - all created
✅ **Backend:** Socket.io infrastructure exists
⚠️ **Database:** MongoDB needs to be started
⚠️ **Backend Server:** Needs to be running

## Quick Start (Local Development)

### 1. Start MongoDB

```bash
# Create data directory
sudo mkdir -p /data/db
sudo chown -R $(whoami) /data/db

# Start MongoDB
mongod --dbpath /data/db --fork --logpath /var/log/mongodb.log
```

### 2. Start Evil Apples Backend

```bash
cd /root/repos/evilapplesserver

# Install dependencies (if not done)
npm install

# Start server (default port 8080)
npm start
# OR with custom port:
# node scripts/evil.js --port 8080
```

### 3. Frontend is Already Running

The web client is running on: **http://localhost:3001/**

Access it via browser automation or deploy to public hosting.

## Production Deployment

### Option 1: All-in-One Server (Quick & Simple)

**Setup:**
1. Deploy backend + frontend on same server
2. Use nginx to serve frontend and proxy API

```nginx
server {
    listen 80;
    server_name play.evilapples.com;
    
    # Frontend
    location / {
        root /var/www/evil-apples-web/dist;
        try_files $uri /index.html;
    }
    
    # Backend API
    location /api {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
    
    # Socket.io
    location /socket.io {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

**Deploy Steps:**
```bash
# Build frontend
cd /root/repos/evilapplesserver/web-client
npm run build

# Copy dist to web server
sudo cp -r dist/* /var/www/evil-apples-web/

# Restart nginx
sudo systemctl restart nginx
```

### Option 2: Vercel + Existing Backend (Fastest)

**Benefits:**
- Zero server management
- Global CDN
- Auto SSL
- Deploy in 2 minutes

**Steps:**
```bash
cd /root/repos/evilapplesserver/web-client

# Install Vercel CLI
npm i -g vercel

# Deploy (will prompt for settings)
vercel

# Set environment variables on Vercel dashboard:
# VITE_API_URL=https://api.evilapples.com
# VITE_SOCKET_URL=https://api.evilapples.com
```

**Backend CORS Setup:**
Add to backend server:
```javascript
app.use(cors({
  origin: 'https://play-evil-apples.vercel.app',
  credentials: true
}));
```

### Option 3: Full AWS (Production-Grade)

**Architecture:**
- Frontend: CloudFront + S3
- Backend: Existing AWS setup
- Database: Existing MongoDB/Redis

**Deploy:**
```bash
# Build
cd web-client
npm run build

# Upload to S3
aws s3 sync dist/ s3://evilapples-web/

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id XXX --paths "/*"
```

## What's Already Built

### Frontend Components ✅

1. **LoginScreen.jsx**
   - Guest login (instant play)
   - Social login placeholders
   - Username entry

2. **GameLobby.jsx**
   - Quick Play button
   - Available games list
   - Player stats

3. **GameRoom.jsx**
   - Active game interface
   - Real-time updates
   - Chat functionality

4. **Cards (QuestionCard, AnswerCard)**
   - Card display components
   - Play animations (ready for styling)

5. **PlayerList.jsx**
   - Player list with scores
   - Judge indicator
   - Status badges

### Backend Support ✅

- Socket.io server (`lib/socket_server.js`)
- PubSub system for real-time events
- Game logic (`lib/game_logic.js`)
- Matchmaking (`lib/matchmaking.js`)
- Authentication (tokens, cookies)

### What's Missing

1. **Backend Web Handlers** - Need to add specific handlers for web clients
2. **Guest Authentication** - Quick guest login API endpoint
3. **CORS Configuration** - Allow web client origin
4. **Environment Setup** - MongoDB seed data

## Today's Goal: Get It Running! 🎯

### Minimum to Launch:

1. ✅ Start MongoDB
2. ✅ Start backend server
3. ✅ Frontend already running (port 3001)
4. ⚠️ Test guest login flow
5. ⚠️ Test game creation
6. 🚀 Deploy frontend to Vercel (2 minutes)

### Testing Locally:

```bash
# 1. Start MongoDB
mongod --fork --dbpath /data/db --logpath /var/log/mongodb.log

# 2. Start backend (already running or):
cd /root/repos/evilapplesserver
npm start -- --port 8080

# 3. Frontend already at http://localhost:3001

# 4. Open browser to localhost:3001
```

## Next Steps

1. **Start MongoDB** - Quick command
2. **Start backend server** - npm start
3. **Test in browser** - Open localhost:3001
4. **Deploy to Vercel** - 2 minute process
5. **Point domain** - play.evilapples.com

**Time estimate:** 30 minutes to live web version! 🚀
