# Quick Start Guide

## Prerequisites Check
✓ Node.js installed (check with `node --version`)
✓ npm installed (check with `npm --version`)

## Installation (First Time Only)

```bash
cd my_streamlit_app/vr-cycling-app
npm install
```

Wait for all dependencies to install (this may take a few minutes).

## Running the Application

### Option 1: Using Batch Files (Windows)

**Terminal 1 - Backend Server:**
```bash
start-server.bat
```

**Terminal 2 - Frontend:**
```bash
start-frontend.bat
```

### Option 2: Using npm Commands

**Terminal 1 - Backend Server:**
```bash
npm run server
```

**Terminal 2 - Frontend:**
```bash
npm start
```

## Access the Application

Once both servers are running:
- Frontend: http://localhost:3000 (opens automatically)
- Backend API: http://localhost:5000

## What You Should See

1. **Backend Terminal**: 
   - "Connected to MQTT broker"
   - "Subscribed to VRcycling/UserA/HIncTime"
   - "Subscribed to VRcycling/UserA/GIncTime"
   - "Loaded XXX path coordinates"
   - "Server running on port 5000"

2. **Frontend Browser**:
   - Beautiful gradient background
   - Left panel with multilingual information and device stats
   - Right panel with interactive map showing the Nuwara Eliya route
   - Two colored markers (blue and red) representing devices
   - Smooth updates every 2 seconds

## Troubleshooting

### Backend won't start
- Make sure port 5000 is not in use
- Check MQTT broker connectivity
- Verify `interpolated_path.csv` exists in parent directory

### Frontend won't start
- Make sure port 3000 is not in use
- Verify npm install completed successfully
- Check that backend is running first

### Map not loading
- Check browser console for errors (F12)
- Verify backend is running and accessible
- Check network requests to http://localhost:5000/api/devices

### Devices not moving
- Verify MQTT connection in backend terminal
- Check if MQTT broker is sending data
- Look for MQTT message updates in backend logs

## Features to Try

1. **Click on device markers** to see detailed position info
2. **Zoom in/out** on the map to see more detail
3. **Watch the progress bars** update in real-time
4. **Observe smooth transitions** - no flickering!

## Stopping the Application

Press `Ctrl+C` in both terminal windows to stop the servers.
