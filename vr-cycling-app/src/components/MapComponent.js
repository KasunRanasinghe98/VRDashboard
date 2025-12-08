import React, { useEffect, useRef } from 'react';
import { MapContainer, TileLayer, Polyline, CircleMarker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import './MapComponent.css';

// Component to update marker positions smoothly
function DeviceMarkers({ devices }) {
  if (!devices) return null;

  return (
    <>
      {/* Colombo (Green) */}
      <CircleMarker
        center={devices.deviceH.position}
        radius={12}
        pathOptions={{
          color: '#2ecc71',
          fillColor: '#2ecc71',
          fillOpacity: 0.8,
          weight: 3
        }}
      >
        <Popup>
          <div className="popup-content">
            <strong>{devices.deviceH.name}</strong>
            <br />
            Position: {devices.deviceH.index}
            <br />
            Lat: {devices.deviceH.position[0].toFixed(6)}
            <br />
            Lon: {devices.deviceH.position[1].toFixed(6)}
          </div>
        </Popup>
      </CircleMarker>

      {/* Kandy (Red) */}
      <CircleMarker
        center={devices.deviceG.position}
        radius={12}
        pathOptions={{
          color: '#e74c3c',
          fillColor: '#e74c3c',
          fillOpacity: 0.9,
          weight: 2
        }}
      >
        <Popup>
          <div className="popup-content">
            <strong>{devices.deviceG.name}</strong>
            <br />
            Position: {devices.deviceG.index}
            <br />
            Lat: {devices.deviceG.position[0].toFixed(6)}
            <br />
            Lon: {devices.deviceG.position[1].toFixed(6)}
          </div>
        </Popup>
      </CircleMarker>
    </>
  );
}

// Component to handle map centering and auto-zoom to fit path
function MapController({ pathData }) {
  const map = useMap();
  const initialFitDone = useRef(false);

  useEffect(() => {
    if (pathData.length > 0 && !initialFitDone.current) {
      // Auto-zoom to fit the entire path with some padding
      const bounds = pathData.map(coord => [coord[0], coord[1]]);
      map.fitBounds(bounds, { padding: [50, 50] });
      initialFitDone.current = true;
    }
  }, [pathData, map]);

  return null;
}

function MapComponent({ devices, pathData }) {
  const defaultCenter = [6.953399599775896, 80.78392973728708];
  const defaultZoom = 16;

  return (
    <div className="map-wrapper">
      <MapContainer
        center={defaultCenter}
        zoom={defaultZoom}
        style={{ height: '100%', width: '100%' }}
        zoomControl={true}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        
        {/* Draw the path - more prominent */}
        {pathData.length > 0 && (
          <Polyline
            positions={pathData}
            pathOptions={{
              color: '#3887d0ff',
              weight: 6,
              opacity: 0.9,
              lineCap: 'round',
              lineJoin: 'round'
            }}
          />
        )}

        {/* Render device markers */}
        <DeviceMarkers devices={devices} />
        
        {/* Map controller - auto-zoom to path */}
        <MapController pathData={pathData} />
      </MapContainer>
    </div>
  );
}

export default MapComponent;
