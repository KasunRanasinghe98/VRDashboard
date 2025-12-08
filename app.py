import streamlit as st
from PIL import Image
import base64
import threading
import paho.mqtt.client as mqtt
import time

# Newly added
import pandas as pd
import folium
from streamlit_folium import st_folium
# from streamlit_autorefresh import st_autorefresh

# Load path points
df = pd.read_csv("interpolated_path.csv")
path_coords = list(zip(df["latitude"], df["longitude"]))  # [(lat, lon), ...]

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(layout="wide", page_title="VR Cycling", page_icon="🚴")

# ------------------ FUNCTIONS ------------------
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ------------------ MQTT CONFIGURATION ------------------
BROKER = "18.140.19.253"
PORT = 8090
USERNAME = "bikeuser"
PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

mqtt_data = {"HIncTime": 0, "GIncTime": 0}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPICS)
    else:
        print(f"Connection failed: {rc}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    try:
        value = int(payload)
        value = max(0, min(301, value))  # Clamp between 0–301
        if topic.endswith("HIncTime"):
            mqtt_data["HIncTime"] = value
        elif topic.endswith("GIncTime"):
            mqtt_data["GIncTime"] = value
    except ValueError:
        pass

def mqtt_loop():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

threading.Thread(target=mqtt_loop, daemon=True).start()

# ------------------ BACKGROUND ------------------
background_image_path = "images/background.jpg"
background_base64 = get_base64_of_bin_file(background_image_path)

st.markdown(f"""
    <style>
    body {{
        font-family: 'Segoe UI', sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{background_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .main-title {{
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        color: #fff;
        background: rgba(0, 0, 0, 0.55);
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }}
    .content-box {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px 30px;
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.25);
        color: #000;
        margin-bottom: 20px;
    }}
    .subheader {{
        font-size: 1.4rem;
        font-weight: 600;
        color: #222;
        text-align: center;
        margin-bottom: 15px;
    }}

    /* --- Progress bar and pointers --- */
    .progress-container {{
        position: relative;
        width: 95%;
        margin: 45px auto 30px auto;
        height: 20px;
    }}

    .progress-bar {{
        position: absolute;
        top: 50%;
        left: 0;
        transform: translateY(-50%);
        width: 100%;
        height: 10px;
        background: linear-gradient(90deg, #ddd, #ccc);
        border-radius: 5px;
        overflow: hidden;
        box-shadow: inset 0 2px 6px rgba(0,0,0,0.2);
    }}

    .pointer {{
        position: absolute;
        top: 50%;
        transform: translate(-50%, -50%);
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background-color: #3498db;
        transition: left 0.5s ease-in-out;
        box-shadow: 0 0 10px rgba(0,0,0,0.4);
        border: 3px solid white;
        z-index: 10;
    }}
    .pointer2 {{
        background-color: #e74c3c;
        z-index: 11;
    }}

    .value-box {{
        text-align: center;
        font-weight: 600;
        font-size: 1.1rem;
        color: #333;
        background: rgba(255,255,255,0.8);
        border-radius: 10px;
        padding: 10px;
        display: inline-block;
        margin-top: 5px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
    }}
    </style>
""", unsafe_allow_html=True)

# ------------------ PAGE TITLE ------------------
st.markdown('<div class="main-title">🚴 VR Cycling — Live Tracking Dashboard</div>', unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([1, 1])

# ---------- LEFT COLUMN ----------
with col1:
    st.markdown('<div class="subheader">🌍 Multilingual Description</div>', unsafe_allow_html=True)

    paragraph_en = """This VR cycling dashboard allows you to track live MQTT data and view progress in real time."""
    paragraph_si = """මෙම VR බයිසිකල් ඩැෂ්බෝර්ඩ් මගින් ඔබට සජීවී MQTT දත්ත නිරීක්ෂණය කළ හැක."""
    paragraph_ta = """இந்த VR சைக்கிளிங் டாஷ்போர்ட் வழியாக நேரடி MQTT தரவை கண்காணிக்க முடியும்."""

    st.markdown(f'<div class="content-box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="content-box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="content-box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# ---------- RIGHT COLUMN ----------
with col2:
    st.markdown('<div class="subheader">🗺️ Live Route — Nuwara Eliya</div>', unsafe_allow_html=True)
    map_placeholder = st.empty()

# Update map every 5 seconds
while True:
    h_value = mqtt_data["HIncTime"]
    g_value = mqtt_data["GIncTime"]

    h_idx = max(0, min(h_value, len(path_coords)-1))
    g_idx = max(0, min(g_value, len(path_coords)-1))

    h_lat, h_lon = path_coords[h_idx]
    g_lat, g_lon = path_coords[g_idx]

    m = folium.Map(location=[6.953399599775896, 80.78392973728708], zoom_start=16)
    folium.CircleMarker([h_lat, h_lon], radius=8, color="blue", fill=True).add_to(m)
    folium.CircleMarker([g_lat, g_lon], radius=8, color="red", fill=True).add_to(m)
    folium.PolyLine(path_coords, weight=4).add_to(m)

    with map_placeholder:
        if "map_key" not in st.session_state:
            st.session_state.map_key = 0

        st.session_state.map_key += 1

        st_folium(
            m,
            width=750,
            height=450,
            returned_objects=[],
            key=f"map_{st.session_state.map_key}"
        )

    time.sleep(10)