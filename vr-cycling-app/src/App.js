import React, { useState, useEffect } from 'react';
import './App.css';
import MapComponent from './components/MapComponent';

function App() {
  const [devices, setDevices] = useState(null);
  const [pathData, setPathData] = useState([]);

  // Use environment variable or fallback to current hostname
  const API_URL = process.env.REACT_APP_API_URL || `${window.location.protocol}//${window.location.hostname}:5000`;

  // Helper function to determine state class for glowing effect
  const getStateClass = (state) => {
    if (!state) return '';
    const stateLower = state.toLowerCase();
    if (stateLower.includes('ready')) return 'state-ready';
    if (stateLower.includes('ingame') || stateLower.includes('racing') || stateLower.includes('playing')) return 'state-ingame';
    if (stateLower.includes('finished') || stateLower.includes('complete')) return 'state-finished';
    return '';
  };

  useEffect(() => {
    // Fetch path data once on mount
    fetch(`${API_URL}/api/path`)
      .then(res => res.json())
      .then(data => {
        setPathData(data.path);
      })
      .catch(err => console.error('Error fetching path:', err));

    // Poll device positions every 0.5 seconds for smooth updates
    const interval = setInterval(() => {
      fetch(`${API_URL}/api/devices`)
        .then(res => res.json())
        .then(data => {
          setDevices(data);
        })
        .catch(err => console.error('Error fetching devices:', err));
    }, 500);

    return () => clearInterval(interval);
  }, [API_URL]);

  return (
    <div className="App">
      {/* Top HUD strip */}
      <div className="top-strip">
        <span>
          <span className="brand-dot"></span>
          Virtual Reality • 5G • Immersive Racing
        </span>
        <span>Colombo &nbsp;Vs.&nbsp; Kandy</span>
      </div>

      <div className="poster-grid">
        {/* LEFT: Content Panel */}
        <section className="left-panel">
          <div>
            <div className="eyebrow">Dialog 5G Experience</div>
            <h1 className="title-main">Virtual Reality Cycling Experience</h1>
            <h2 className="title-sub">Colombo vs Kandy</h2>

            <p className="subtitle">
              <font size = "2.5"><b> VR Cycling </b> offers an immersive real-world riding experience, 
              allowing you to pedal freely through realistic 360° environments. 
              It effectively bridges the gap between virtual simulation and real-world cycling.</font>
            </p>

            <p className="subtitle">
              <font size = "2.5"><b> VR cycling </b> ඔබට සජීවීකරණයකින් ඔබ්බට ගිය, 360° පරිසරයන් හරහා නිදහසේ සයිකල් පැදීමේ අත්දැකීමක් ලබා දෙයි. 
              මෙමගින් පරිගණක මගින් නිර්මාණය කරන ලද අනුකරණවල සහ ස්වභාවික ලෝකයේ සයිකල් පැදීම අතර ඇති පරතරය කාර්යක්ෂමව පුරවා දේ.</font>
            </p>

            <p className="subtitle">
                <font size = "2"><b> VR Cycling </b> </font> <font size = "1.5"> உங்களுக்கு உண்மையான சைக்கிள் சவாரி போன்ற
                அனுபவத்தை வழங்கும் ஒரு மெய்நிகர் நடைமுறை. 360° சூழல்களில் முழு சுதந்திரத்துடன் சைக்கிள்
                  ஓட்ட அனுமதிப்பதன் மூலம், இது மெய்நிகர் உருவகமும் நிஜ உலக சவாரி அனுபவமும் இடையிலான
                  இடைவெளியை திறம்பட இணைக்கிறது</font>
            </p>

          </div>

          {/* Rider Status Cards - Single Row */}
          <div className="ready-indicator">
            <div className="ready-label">Location Rider Status</div>
            <div className="ready-pills">
              <div className={`ready-pill ${getStateClass(devices?.deviceH.state)}`}>
                <span className="ready-dot"></span>
                Colombo {devices?.deviceH.state || 'Loading...'}
              </div>
              <div className={`ready-pill ${getStateClass(devices?.deviceG.state)}`}>
                <span className="ready-dot"></span>
                Kandy {devices?.deviceG.state || 'Loading...'}
              </div>
            </div>
          </div>

          {/* Bottom Illustration and Logos */}
          <div className="bottom-illustration-wrapper">
            <img 
              src="/logos/steps.png" 
              alt="VR Cycling Steps" 
              className="bottom-illustration"
              onError={(e) => e.target.style.display = 'none'}
            />
            <div className="bottom-logos">
              <div className="logo-tile">
                <img src="/logos/dialog.png" alt="Dialog" onError={(e) => e.target.style.display = 'none'} />
              </div>
              <div className="logo-tile">
                <img src="/logos/entc.png" alt="ENTC" onError={(e) => e.target.style.display = 'none'} />
              </div>
              <div className="logo-tile">
                <img src="/logos/partner.png" alt="Partner" onError={(e) => e.target.style.display = 'none'} />
              </div>
            </div>
          </div>
        </section>

        {/* RIGHT: Map Display */}
        <section className="right-panel">
          <div className="map-frame-wrapper">
            <div className="map-frame-inner">
              {/* HUD corners */}
              <div className="hud-corner tl"></div>
              <div className="hud-corner tr"></div>
              <div className="hud-corner bl"></div>
              <div className="hud-corner br"></div>

              <div className="badge-live">
                <span className="badge-live-dot"></span>
                LIVE DEMO • 5G LINK
              </div>

              {/* Map Component */}
              <MapComponent devices={devices} pathData={pathData} />
            </div>
          </div>

          {/* Legend - Simplified */}
          <div className="map-legend">
            <div className="legend-items">
              <div className="legend-item">
                <div className="legend-color" style={{ color: '#2ecc71' }}></div>
                <span className="legend-name">Colombo</span>
              </div>
              <div className="legend-item">
                <div className="legend-color" style={{ color: '#e74c3c' }}></div>
                <span className="legend-name">Kandy</span>
              </div>
            </div>
          </div>

          {/* Feature Chips */}
          <div className="chips-row">
            <div className="chip">
              <span className="chip-dot"></span>
              Live via 5G
            </div>
            <div className="chip">
              <span className="chip-dot"></span>
              Sri Lankan Routes
            </div>
            <div className="chip">
              <span className="chip-dot"></span>
              Immersive
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default App;
