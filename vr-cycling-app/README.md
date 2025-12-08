# VR Cycling Dashboard - React + Leaflet

A modern, real-time tracking dashboard for VR cycling devices built with React and Leaflet. This application provides smooth, flicker-free map updates compared to the previous Streamlit implementation.

## Features

- **Real-time Device Tracking**: Live MQTT data updates for two cycling devices
- **Smooth Map Rendering**: React + Leaflet provides seamless updates without flickering
- **Modern UI**: Beautiful gradient backgrounds, smooth animations, and responsive design
- **Multilingual Support**: Information available in English, Sinhala, and Tamil
- **Interactive Map**: Click on device markers to view detailed position information
- **Progress Tracking**: Visual progress bars showing device advancement along the route

## Tech Stack

- **Frontend**: React 18, React-Leaflet, Leaflet
- **Backend**: Node.js, Express
- **Communication**: MQTT for live device data
- **Map Data**: OpenStreetMap tiles

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn

## Installation

1. Navigate to the project directory:
```bash
cd my_streamlit_app/vr-cycling-app
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

### Step 1: Start the Backend Server

The backend server connects to MQTT and serves device position data:

```bash
npm run server
```

The server will run on `http://localhost:5000`

### Step 2: Start the React Frontend

In a new terminal, start the React development server:

```bash
npm start
```

The application will open in your browser at `http://localhost:3000`

## How It Works

1. **Backend Server**: 
   - Connects to the MQTT broker at `mqtt://18.140.19.253:8090`
   - Subscribes to device topics: `VRcycling/UserA/HIncTime` and `VRcycling/UserA/GIncTime`
   - Loads the path coordinates from `interpolated_path.csv`
   - Provides REST API endpoints for device positions and path data

2. **Frontend Application**:
   - Polls the backend every 2 seconds for device positions
   - Renders the map with Leaflet showing the route and device markers
   - Updates device positions smoothly without re-rendering the entire map
   - Displays device statistics and progress in the side panel

## API Endpoints

- `GET /api/path` - Returns the complete route path coordinates
- `GET /api/devices` - Returns current positions of both devices

## Configuration

MQTT settings can be modified in `backend/server.js`:
- `BROKER`: MQTT broker URL
- `USERNAME`: MQTT username
- `PASSWORD`: MQTT password
- `TOPICS`: Array of MQTT topics to subscribe to

## Advantages Over Streamlit

1. **No Flickering**: React's virtual DOM efficiently updates only changed elements
2. **Better Performance**: Smoother animations and transitions
3. **More Control**: Fine-grained control over map rendering and updates
4. **Modern UI**: Enhanced styling with CSS gradients and animations
5. **Scalability**: Easier to add new features and components

## Troubleshooting

If you encounter issues:

1. **MQTT Connection Failed**: Check if the MQTT broker is accessible
2. **CSV File Not Found**: Ensure `interpolated_path.csv` is in the correct location
3. **Port Already in Use**: Change the port in `backend/server.js` or stop conflicting services

## License

This project is part of the VR Cycling application suite.
