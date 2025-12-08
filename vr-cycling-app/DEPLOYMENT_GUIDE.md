# Deployment Guide - VR Cycling Dashboard

## Fixing the "Map/Route Not Visible on Other Devices" Issue

### Problem
The map route (blue line) and device markers are only visible on the hosting machine, but not on other devices accessing the app.

### Root Cause
The app was hardcoded to fetch data from `localhost:5000`, which only works on the server machine itself.

### Solution Implemented
The API URL now dynamically uses the server's hostname/IP address.

---

## Deployment Steps

### 1. On Your Linux Server

#### Option A: Using Environment Variable (Recommended for Production)

1. Create a `.env` file in the `vr-cycling-app` directory:
```bash
cd vr-cycling-app
nano .env
```

2. Add your server's IP address or domain:
```
REACT_APP_API_URL=http://YOUR_SERVER_IP:5000
```
Example:
```
REACT_APP_API_URL=http://192.168.1.100:5000
```

3. Rebuild the React app:
```bash
npm run build
```

#### Option B: Automatic Detection (Works if frontend and backend on same server)

If you don't create a `.env` file, the app will automatically detect the hostname from the browser URL.

- If accessed via `http://192.168.1.100:3000`, it will try `http://192.168.1.100:5000`
- If accessed via `http://your-domain.com:3000`, it will try `http://your-domain.com:5000`

---

### 2. Backend Server Configuration

Make sure your backend server (server.js) allows external connections:

```javascript
// In backend/server.js
const PORT = 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});
```

The `'0.0.0.0'` parameter allows external connections.

---

### 3. Firewall Configuration

On your Linux server, open port 5000:

```bash
# For UFW (Ubuntu)
sudo ufw allow 5000

# For firewalld (CentOS/RHEL)
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload
```

---

### 4. CORS Configuration (Already Done)

The backend already has CORS enabled in server.js:
```javascript
const cors = require('cors');
app.use(cors());
```

---

## Testing

1. **On the server machine:**
```bash
# Start backend
cd vr-cycling-app
npm run server

# In another terminal, start frontend
npm start
# OR if using build
npx serve -s build -l 3000
```

2. **From another device on the same network:**
   - Access: `http://YOUR_SERVER_IP:3000`
   - The map route and markers should now be visible!

---

## Production Deployment Options

### Option 1: Serve from Same Server
Build and serve the React app:
```bash
npm run build
npx serve -s build -l 80
```

### Option 2: Using Nginx
1. Build the React app
2. Configure Nginx:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /path/to/vr-cycling-app/build;
        index index.html;
        try_files $uri /index.html;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

### Option 3: PM2 for Process Management
```bash
# Install PM2
npm install -g pm2

# Start backend with PM2
cd backend
pm2 start server.js --name "vr-cycling-backend"

# Start frontend with PM2
cd ..
pm2 serve build 3000 --name "vr-cycling-frontend"

# Save PM2 configuration
pm2 save
pm2 startup
```

---

## Troubleshooting

### Issue: Still not seeing map/markers on other devices

1. **Check browser console** (F12) on the remote device:
   - Look for network errors
   - Verify the API URL being used

2. **Verify backend is accessible:**
```bash
# From another device
curl http://YOUR_SERVER_IP:5000/api/path
```

3. **Check backend logs:**
```bash
# Should see incoming requests
npm run server
```

4. **Verify both frontend and backend are running:**
```bash
# Check if processes are running
netstat -tulpn | grep :3000
netstat -tulpn | grep :5000
```

### Issue: CORS errors

If you see CORS errors, ensure your backend has:
```javascript
const cors = require('cors');
app.use(cors());
```

---

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `REACT_APP_API_URL` | Backend API URL | `http://192.168.1.100:5000` |

---

## Quick Commands

```bash
# Development
npm start                    # Start frontend dev server
npm run server              # Start backend server

# Production Build
npm run build               # Build for production
npx serve -s build -l 3000  # Serve production build

# Process Management
pm2 start ecosystem.config.js  # Start with PM2
pm2 logs                       # View logs
pm2 restart all                # Restart all processes
```

---

## Notes

- The frontend will automatically use the correct hostname when accessed
- Make sure port 5000 (backend) and your frontend port are accessible
- For production, always use environment variables for configuration
- Keep your `.env` file out of version control (it's already in .gitignore)
