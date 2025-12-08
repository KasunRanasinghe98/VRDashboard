# # import streamlit as st
# # from PIL import Image
# # import base64
# # import threading
# # import paho.mqtt.client as mqtt
# # import time

# # # Newly added
# # import pandas as pd
# # import folium
# # from streamlit_folium import st_folium

# # # Load path points
# # df = pd.read_csv("interpolated_path.csv")
# # path_coords = list(zip(df["latitude"], df["longitude"]))  # [(lat, lon), ...]

# # # ------------------ PAGE SETTINGS ------------------
# # st.set_page_config(layout="wide", page_title="VR Cycling", page_icon="🚴")

# # # ------------------ FUNCTIONS ------------------
# # def get_base64_of_bin_file(bin_file):
# #     with open(bin_file, "rb") as f:
# #         data = f.read()
# #     return base64.b64encode(data).decode()

# # # ------------------ MQTT CONFIGURATION ------------------
# # BROKER = "18.140.19.253"
# # PORT = 8090
# # USERNAME = "bikeuser"
# # PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
# # TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

# # mqtt_data = {"HIncTime": 0, "GIncTime": 0}

# # def on_connect(client, userdata, flags, rc):
# #     if rc == 0:
# #         client.subscribe(TOPICS)
# #     else:
# #         print(f"Connection failed: {rc}")

# # def on_message(client, userdata, msg):
# #     topic = msg.topic
# #     payload = msg.payload.decode("utf-8")
# #     try:
# #         value = int(payload)
# #         value = max(0, min(301, value))  # Clamp between 0–301
# #         if topic.endswith("HIncTime"):
# #             mqtt_data["HIncTime"] = value
# #         elif topic.endswith("GIncTime"):
# #             mqtt_data["GIncTime"] = value
# #     except ValueError:
# #         pass

# # def mqtt_loop():
# #     client = mqtt.Client()
# #     client.username_pw_set(USERNAME, PASSWORD)
# #     client.on_connect = on_connect
# #     client.on_message = on_message
# #     client.connect(BROKER, PORT, 60)
# #     client.loop_forever()

# # threading.Thread(target=mqtt_loop, daemon=True).start()

# # # ------------------ BACKGROUND ------------------
# # background_image_path = "images/background.jpg"
# # background_base64 = get_base64_of_bin_file(background_image_path)

# # st.markdown(f"""
# #     <style>
# #     body {{
# #         font-family: 'Segoe UI', sans-serif;
# #     }}
# #     [data-testid="stAppViewContainer"] {{
# #         background-image: url("data:image/jpg;base64,{background_base64}");
# #         background-size: cover;
# #         background-position: center;
# #         background-repeat: no-repeat;
# #     }}
# #     .main-title {{
# #         font-size: 2.2rem;
# #         font-weight: bold;
# #         text-align: center;
# #         color: #fff;
# #         background: rgba(0, 0, 0, 0.55);
# #         padding: 15px;
# #         border-radius: 12px;
# #         box-shadow: 0 4px 10px rgba(0,0,0,0.3);
# #         margin-bottom: 25px;
# #     }}
# #     .content-box {{
# #         background-color: rgba(255, 255, 255, 0.85);
# #         padding: 25px 30px;
# #         border-radius: 20px;
# #         box-shadow: 0 6px 15px rgba(0,0,0,0.25);
# #         color: #000;
# #         margin-bottom: 20px;
# #     }}
# #     .subheader {{
# #         font-size: 1.4rem;
# #         font-weight: 600;
# #         color: #222;
# #         text-align: center;
# #         margin-bottom: 15px;
# #     }}

# #     /* --- Progress bar and pointers --- */
# #     .progress-container {{
# #         position: relative;
# #         width: 95%;
# #         margin: 45px auto 30px auto;
# #         height: 20px;
# #     }}

# #     .progress-bar {{
# #         position: absolute;
# #         top: 50%;
# #         left: 0;
# #         transform: translateY(-50%);
# #         width: 100%;
# #         height: 10px;
# #         background: linear-gradient(90deg, #ddd, #ccc);
# #         border-radius: 5px;
# #         overflow: hidden;
# #         box-shadow: inset 0 2px 6px rgba(0,0,0,0.2);
# #     }}

# #     .pointer {{
# #         position: absolute;
# #         top: 50%;
# #         transform: translate(-50%, -50%);
# #         width: 22px;
# #         height: 22px;
# #         border-radius: 50%;
# #         background-color: #3498db;
# #         transition: left 0.5s ease-in-out;
# #         box-shadow: 0 0 10px rgba(0,0,0,0.4);
# #         border: 3px solid white;
# #         z-index: 10;
# #     }}
# #     .pointer2 {{
# #         background-color: #e74c3c;
# #         z-index: 11;
# #     }}

# #     .value-box {{
# #         text-align: center;
# #         font-weight: 600;
# #         font-size: 1.1rem;
# #         color: #333;
# #         background: rgba(255,255,255,0.8);
# #         border-radius: 10px;
# #         padding: 10px;
# #         display: inline-block;
# #         margin-top: 5px;
# #         box-shadow: 0 3px 6px rgba(0,0,0,0.2);
# #     }}
# #     </style>
# # """, unsafe_allow_html=True)

# # # ------------------ PAGE TITLE ------------------
# # st.markdown('<div class="main-title">🚴 VR Cycling — Live Tracking Dashboard</div>', unsafe_allow_html=True)

# # # ------------------ LAYOUT ------------------
# # col1, col2 = st.columns([1, 1])

# # # ---------- LEFT COLUMN ----------
# # with col1:
# #     st.markdown('<div class="subheader">🌍 Multilingual Description</div>', unsafe_allow_html=True)

# #     paragraph_en = """This VR cycling dashboard allows you to track live MQTT data and view progress in real time."""
# #     paragraph_si = """මෙම VR බයිසිකල් ඩැෂ්බෝර්ඩ් මගින් ඔබට සජීවී MQTT දත්ත නිරීක්ෂණය කළ හැක."""
# #     paragraph_ta = """இந்த VR சைக்கிளிங் டாஷ்போர்ட் வழியாக நேரடி MQTT தரவை கண்காணிக்க முடியும்."""

# #     st.markdown(f'<div class="content-box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
# #     st.markdown(f'<div class="content-box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
# #     st.markdown(f'<div class="content-box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# # # # ---------- RIGHT COLUMN ----------
# # # with col2:
# # #     st.markdown('<div class="subheader">📊 Real-time MQTT Visual</div>', unsafe_allow_html=True)
# # #     bar_placeholder = st.empty()

# # # # ---------- NEW RIGHT COLUMN ----------
# # # with col2:
# # #     st.markdown('<div class="subheader">🗺️ Live Route — Nuwara Eliya</div>', unsafe_allow_html=True)
# # #     map_placeholder = st.empty()

# # # # ------------------ NEW DISPLAY LOOP ------------------
# # # while True:
# # #     h_value = mqtt_data["HIncTime"]
# # #     g_value = mqtt_data["GIncTime"]

# # #     # Clip values safely
# # #     h_idx = max(0, min(h_value, len(path_coords)-1))
# # #     g_idx = max(0, min(g_value, len(path_coords)-1))

# # #     # Get coordinates
# # #     h_lat, h_lon = path_coords[h_idx]
# # #     g_lat, g_lon = path_coords[g_idx]

# # #     # Center map at rider A - feel free to change
# # #     m = folium.Map(location=[h_lat, h_lon], zoom_start=17)

# # #     # Rider A marker (Blue)
# # #     folium.CircleMarker(
# # #         location=[h_lat, h_lon],
# # #         radius=8,
# # #         popup=f"Rider A — {h_idx} / 301",
# # #         color="blue",
# # #         fill=True,
# # #         fill_opacity=0.9
# # #     ).add_to(m)

# # #     # Rider B marker (Red)
# # #     folium.CircleMarker(
# # #         location=[g_lat, g_lon],
# # #         radius=8,
# # #         popup=f"Rider B — {g_idx} / 301",
# # #         color="red",
# # #         fill=True,
# # #         fill_opacity=0.9
# # #     ).add_to(m)

# # #     # Draw path polyline
# # #     folium.PolyLine(path_coords, weight=4).add_to(m)

# # #     # Show map
# # #     with col2:
# # #         map_placeholder = st_folium(m, width=750, height=450, key="main_map")

# # #     time.sleep(1)

# # # ---------- NEW RIGHT COLUMN ----------
# # with col2:
# #     st.markdown('<div class="subheader">🗺️ Live Route — Nuwara Eliya</div>', unsafe_allow_html=True)
# #     map_placeholder = st.empty()

# # # ------------------ NEW DISPLAY LOOP ------------------
# # for _ in range(3600):
# #     h_value = mqtt_data["HIncTime"]
# #     g_value = mqtt_data["GIncTime"]

# #     h_idx = max(0, min(h_value, len(path_coords)-1))
# #     g_idx = max(0, min(g_value, len(path_coords)-1))

# #     h_lat, h_lon = path_coords[h_idx]
# #     g_lat, g_lon = path_coords[g_idx]

# #     # Create the map dynamically
# #     m = folium.Map(location=[h_lat, h_lon], zoom_start=17)

# #     folium.CircleMarker(
# #         location=[h_lat, h_lon],
# #         radius=8,
# #         popup=f"Rider A — {h_idx} / 301",
# #         color="blue",
# #         fill=True,
# #         fill_opacity=0.9
# #     ).add_to(m)

# #     folium.CircleMarker(
# #         location=[g_lat, g_lon],
# #         radius=8,
# #         popup=f"Rider B — {g_idx} / 301",
# #         color="red",
# #         fill=True,
# #         fill_opacity=0.9
# #     ).add_to(m)

# #     folium.PolyLine(path_coords, weight=4).add_to(m)

# #     # Update same placeholder (no duplicate key)
# #     with col2:
# #         map_placeholder.empty()  # clear old one
# #         map_placeholder = st_folium(m, width=750, height=450, key="main_map")

# #     time.sleep(1)






















# # # import streamlit as st
# # # from PIL import Image
# # # import base64
# # # import threading
# # # import paho.mqtt.client as mqtt
# # # import time

# # # # ------------------ PAGE SETTINGS ------------------
# # # st.set_page_config(layout="wide", page_title="VR Cycling")

# # # # ------------------ FUNCTIONS ------------------
# # # def get_base64_of_bin_file(bin_file):
# # #     """Convert local image file to base64 string"""
# # #     with open(bin_file, "rb") as f:
# # #         data = f.read()
# # #     return base64.b64encode(data).decode()

# # # # ------------------ MQTT CONFIGURATION ------------------
# # # BROKER = "18.140.19.253"
# # # PORT = 8090
# # # USERNAME = "bikeuser"
# # # PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
# # # TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

# # # mqtt_data = {"HIncTime": 0, "GIncTime": 0}

# # # def on_connect(client, userdata, flags, rc):
# # #     if rc == 0:
# # #         client.subscribe(TOPICS)
# # #     else:
# # #         print(f"Connection failed: {rc}")

# # # def on_message(client, userdata, msg):
# # #     topic = msg.topic
# # #     payload = msg.payload.decode("utf-8")
# # #     try:
# # #         value = int(payload)
# # #         value = max(0, min(301, value))  # Clamp between 0–301
# # #         if topic.endswith("HIncTime"):
# # #             mqtt_data["HIncTime"] = value
# # #         elif topic.endswith("GIncTime"):
# # #             mqtt_data["GIncTime"] = value
# # #     except ValueError:
# # #         pass  # Ignore non-numeric payloads

# # # def mqtt_loop():
# # #     client = mqtt.Client()
# # #     client.username_pw_set(USERNAME, PASSWORD)
# # #     client.on_connect = on_connect
# # #     client.on_message = on_message
# # #     client.connect(BROKER, PORT, 60)
# # #     client.loop_forever()

# # # threading.Thread(target=mqtt_loop, daemon=True).start()

# # # # ------------------ IMAGE FILES ------------------
# # # background_image_path = "images/background.jpg"
# # # background_base64 = get_base64_of_bin_file(background_image_path)

# # # # ------------------ CUSTOM CSS ------------------
# # # st.markdown(f"""
# # #     <style>
# # #     [data-testid="stAppViewContainer"] {{
# # #         background-image: url("data:image/jpg;base64,{background_base64}");
# # #         background-size: cover;
# # #         background-position: center;
# # #         background-repeat: no-repeat;
# # #     }}
# # #     .box {{
# # #         background-color: rgba(255, 255, 255, 0.8);
# # #         padding: 20px 25px;
# # #         border-radius: 15px;
# # #         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
# # #         margin-bottom: 20px;
# # #         color: #000000;
# # #     }}
# # #     .subheader {{
# # #         font-size: 1.4rem;
# # #         font-weight: 600;
# # #         color: #222;
# # #         background-color: rgba(240, 240, 240, 0.8);
# # #         border-radius: 12px;
# # #         padding: 10px 15px;
# # #         text-align: center;
# # #         margin-bottom: 15px;
# # #         box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
# # #     }}
# # #     .progress-bar {{
# # #         position: relative;
# # #         width: 90%;
# # #         height: 10px;
# # #         background: rgba(0,0,0,0.15);
# # #         border-radius: 5px;
# # #         margin: 30px auto;
# # #     }}
# # #     .pointer {{
# # #         position: absolute;
# # #         top: -7px;
# # #         width: 20px;
# # #         height: 20px;
# # #         border-radius: 50%;
# # #         background-color: #3498db;
# # #         transition: left 0.5s ease-in-out;
# # #         box-shadow: 0 0 6px rgba(0,0,0,0.3);
# # #     }}
# # #     .pointer2 {{
# # #         background-color: #e74c3c;
# # #     }}
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # ------------------ LAYOUT ------------------
# # # col1, col2 = st.columns(2)

# # # with col1:
# # #     st.markdown('<div class="subheader">🚴 VR Cycling ...</div>', unsafe_allow_html=True)

# # #     paragraph_en = """This is a sample paragraph in English. 
# # #     It represents the same content translated into different languages."""
# # #     paragraph_si = """මෙය ඉංග්‍රීසි පාඨයේ සිංහල පරිවර්තනයකි. 
# # #     එකම අන්තර්ගතය විවිධ භාෂාවලින් නිරූපණය කරයි."""
# # #     paragraph_ta = """இது ஆங்கில பத்தி தமிழ் மொழிபெயர்ப்பு ஆகும். 
# # #     அதே உள்ளடக்கத்தை வேறு மொழிகளில் வெளிப்படுத்துகிறது."""

# # #     st.markdown(f'<div class="box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
# # #     st.markdown(f'<div class="box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
# # #     st.markdown(f'<div class="box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# # # with col2:
# # #     st.markdown('<div class="subheader">About This Section</div>', unsafe_allow_html=True)
# # #     st.markdown(
# # #         '<div class="box">This section displays some text at the top and dynamic MQTT visual below it.</div>',
# # #         unsafe_allow_html=True
# # #     )

# # #     st.markdown('<div class="subheader">Live MQTT Visual</div>', unsafe_allow_html=True)
# # #     bar_placeholder = st.empty()

# # # # ------------------ DISPLAY LOOP ------------------
# # # while True:
# # #     h_value = mqtt_data["HIncTime"]
# # #     g_value = mqtt_data["GIncTime"]

# # #     # Convert 0–301 to percentage
# # #     h_pos = (h_value / 301) * 100
# # #     g_pos = (g_value / 301) * 100

# # #     html_content = f"""
# # #     <div class="box">
# # #         <div class="progress-bar">
# # #             <div class="pointer" style="left:{h_pos}%;"></div>
# # #             <div class="pointer pointer2" style="left:{g_pos}%;"></div>
# # #         </div>
# # #         <b>HIncTime:</b> {h_value} &nbsp;&nbsp; | &nbsp;&nbsp; <b>GIncTime:</b> {g_value}
# # #     </div>
# # #     """

# # #     bar_placeholder.markdown(html_content, unsafe_allow_html=True)
# # #     time.sleep(1)

















# # # import streamlit as st
# # # from PIL import Image
# # # import base64
# # # import threading
# # # import paho.mqtt.client as mqtt
# # # import time

# # # # ------------------ PAGE SETTINGS ------------------
# # # st.set_page_config(layout="wide", page_title="VR Cycling", page_icon="🚴")

# # # # ------------------ FUNCTIONS ------------------
# # # def get_base64_of_bin_file(bin_file):
# # #     with open(bin_file, "rb") as f:
# # #         data = f.read()
# # #     return base64.b64encode(data).decode()

# # # # ------------------ MQTT CONFIGURATION ------------------
# # # BROKER = "18.140.19.253"
# # # PORT = 8090
# # # USERNAME = "bikeuser"
# # # PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
# # # TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

# # # mqtt_data = {"HIncTime": 0, "GIncTime": 0}

# # # def on_connect(client, userdata, flags, rc):
# # #     if rc == 0:
# # #         client.subscribe(TOPICS)
# # #     else:
# # #         print(f"Connection failed: {rc}")

# # # def on_message(client, userdata, msg):
# # #     topic = msg.topic
# # #     payload = msg.payload.decode("utf-8")
# # #     try:
# # #         value = int(payload)
# # #         value = max(0, min(301, value))  # Clamp between 0–301
# # #         if topic.endswith("HIncTime"):
# # #             mqtt_data["HIncTime"] = value
# # #         elif topic.endswith("GIncTime"):
# # #             mqtt_data["GIncTime"] = value
# # #     except ValueError:
# # #         pass

# # # def mqtt_loop():
# # #     client = mqtt.Client()
# # #     client.username_pw_set(USERNAME, PASSWORD)
# # #     client.on_connect = on_connect
# # #     client.on_message = on_message
# # #     client.connect(BROKER, PORT, 60)
# # #     client.loop_forever()

# # # threading.Thread(target=mqtt_loop, daemon=True).start()

# # # # ------------------ BACKGROUND ------------------
# # # background_image_path = "images/background.jpg"
# # # background_base64 = get_base64_of_bin_file(background_image_path)

# # # st.markdown(f"""
# # #     <style>
# # #     body {{
# # #         font-family: 'Segoe UI', sans-serif;
# # #     }}
# # #     [data-testid="stAppViewContainer"] {{
# # #         background-image: url("data:image/jpg;base64,{background_base64}");
# # #         background-size: cover;
# # #         background-position: center;
# # #         background-repeat: no-repeat;
# # #     }}
# # #     .main-title {{
# # #         font-size: 2.2rem;
# # #         font-weight: bold;
# # #         text-align: center;
# # #         color: #fff;
# # #         background: rgba(0, 0, 0, 0.55);
# # #         padding: 15px;
# # #         border-radius: 12px;
# # #         box-shadow: 0 4px 10px rgba(0,0,0,0.3);
# # #         margin-bottom: 25px;
# # #     }}
# # #     .content-box {{
# # #         background-color: rgba(255, 255, 255, 0.85);
# # #         padding: 25px 30px;
# # #         border-radius: 20px;
# # #         box-shadow: 0 6px 15px rgba(0,0,0,0.25);
# # #         color: #000;
# # #         margin-bottom: 20px;
# # #     }}
# # #     .subheader {{
# # #         font-size: 1.4rem;
# # #         font-weight: 600;
# # #         color: #222;
# # #         text-align: center;
# # #         margin-bottom: 15px;
# # #     }}

# # #     /* --- Progress bar and pointers --- */
# # #     .progress-container {{
# # #         position: relative;
# # #         width: 95%;
# # #         margin: 45px auto 30px auto;
# # #         height: 20px;
# # #     }}

# # #     .progress-bar {{
# # #         position: absolute;
# # #         top: 50%;
# # #         left: 0;
# # #         transform: translateY(-50%);
# # #         width: 100%;
# # #         height: 10px;
# # #         background: linear-gradient(90deg, #ddd, #ccc);
# # #         border-radius: 5px;
# # #         overflow: hidden;
# # #         box-shadow: inset 0 2px 6px rgba(0,0,0,0.2);
# # #     }}

# # #     .pointer {{
# # #         position: absolute;
# # #         top: 50%;
# # #         transform: translate(-50%, -50%);
# # #         width: 22px;
# # #         height: 22px;
# # #         border-radius: 50%;
# # #         background-color: #3498db;
# # #         transition: left 0.5s ease-in-out;
# # #         box-shadow: 0 0 10px rgba(0,0,0,0.4);
# # #         border: 3px solid white;
# # #         z-index: 10;
# # #     }}
# # #     .pointer2 {{
# # #         background-color: #e74c3c;
# # #         z-index: 11;
# # #     }}

# # #     .value-box {{
# # #         text-align: center;
# # #         font-weight: 600;
# # #         font-size: 1.1rem;
# # #         color: #333;
# # #         background: rgba(255,255,255,0.8);
# # #         border-radius: 10px;
# # #         padding: 10px;
# # #         display: inline-block;
# # #         margin-top: 5px;
# # #         box-shadow: 0 3px 6px rgba(0,0,0,0.2);
# # #     }}
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # ------------------ PAGE TITLE ------------------
# # # st.markdown('<div class="main-title">🚴 VR Cycling — Live Tracking Dashboard</div>', unsafe_allow_html=True)

# # # # ------------------ LAYOUT ------------------
# # # col1, col2 = st.columns([1, 1])

# # # # ---------- LEFT COLUMN ----------
# # # with col1:
# # #     st.markdown('<div class="subheader">🌍 Multilingual Description</div>', unsafe_allow_html=True)

# # #     paragraph_en = """This VR cycling dashboard allows you to track live MQTT data and view progress in real time."""
# # #     paragraph_si = """මෙම VR බයිසිකල් ඩැෂ්බෝර්ඩ් මගින් ඔබට සජීවී MQTT දත්ත නිරීක්ෂණය කළ හැක."""
# # #     paragraph_ta = """இந்த VR சைக்கிளிங் டாஷ்போர்ட் வழியாக நேரடி MQTT தரவை கண்காணிக்க முடியும்."""

# # #     st.markdown(f'<div class="content-box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
# # #     st.markdown(f'<div class="content-box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
# # #     st.markdown(f'<div class="content-box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# # # # ---------- RIGHT COLUMN ----------
# # # with col2:
# # #     st.markdown('<div class="subheader">📊 Real-time MQTT Visual</div>', unsafe_allow_html=True)
# # #     bar_placeholder = st.empty()

# # # # ------------------ DISPLAY LOOP ------------------
# # # while True:
# # #     h_value = mqtt_data["HIncTime"]
# # #     g_value = mqtt_data["GIncTime"]

# # #     h_pos = (h_value / 301) * 100
# # #     g_pos = (g_value / 301) * 100

# # #     html_content = f"""
# # #     <div class="content-box" style="text-align:center;">
# # #         <div class="progress-container">
# # #             <div class="progress-bar"></div>
# # #             <div class="pointer" style="left:{h_pos}%;"></div>
# # #             <div class="pointer pointer2" style="left:{g_pos}%;"></div>
# # #         </div>
# # #         <div>
# # #             <span class="value-box" style="color:#3498db;">Kandy: {(h_value / 301)*1000} m</span>
# # #             &nbsp;&nbsp;
# # #             <span class="value-box" style="color:#e74c3c;">Colombo: {(g_value / 301)*1000} m</span>
# # #         </div>
# # #     </div>
# # #     """



# # #     bar_placeholder.markdown(html_content, unsafe_allow_html=True)
# # #     time.sleep(1)















# # # import streamlit as st
# # # from PIL import Image
# # # import base64
# # # import threading
# # # import paho.mqtt.client as mqtt
# # # import numpy as np
# # # import plotly.graph_objects as go
# # # from streamlit_autorefresh import st_autorefresh

# # # # ------------------ PAGE SETTINGS ------------------
# # # st.set_page_config(layout="wide", page_title="VR Cycling")

# # # # ------------------ FUNCTIONS ------------------
# # # def get_base64_of_bin_file(bin_file):
# # #     """Convert local image file to base64 string"""
# # #     with open(bin_file, "rb") as f:
# # #         data = f.read()
# # #     return base64.b64encode(data).decode()

# # # # ------------------ MQTT CONFIGURATION ------------------
# # # BROKER = "18.140.19.253"
# # # PORT = 8090
# # # USERNAME = "bikeuser"
# # # PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
# # # TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

# # # # Global data container (thread-safe)
# # # mqtt_data = {"HIncTime": 0, "GIncTime": 0}
# # # mqtt_lock = threading.Lock()

# # # def on_connect(client, userdata, flags, rc):
# # #     if rc == 0:
# # #         print("✅ Connected to MQTT broker")
# # #         client.subscribe(TOPICS)
# # #     else:
# # #         print(f"❌ Connection failed with code {rc}")

# # # def on_message(client, userdata, msg):
# # #     topic = msg.topic
# # #     payload = msg.payload.decode("utf-8")
# # #     try:
# # #         value = int(payload)
# # #         value = max(0, min(301, value))  # Clamp values between 0–301
# # #         with mqtt_lock:
# # #             if topic.endswith("HIncTime"):
# # #                 mqtt_data["HIncTime"] = value
# # #             elif topic.endswith("GIncTime"):
# # #                 mqtt_data["GIncTime"] = value
# # #     except ValueError:
# # #         pass  # ignore invalid payloads

# # # def mqtt_loop():
# # #     client = mqtt.Client()
# # #     client.username_pw_set(USERNAME, PASSWORD)
# # #     client.on_connect = on_connect
# # #     client.on_message = on_message
# # #     client.connect(BROKER, PORT, 60)
# # #     client.loop_forever()

# # # # Start MQTT thread only once
# # # if "mqtt_thread_started" not in st.session_state:
# # #     t = threading.Thread(target=mqtt_loop, daemon=True)
# # #     t.start()
# # #     st.session_state.mqtt_thread_started = True

# # # # ------------------ IMAGE FILES ------------------
# # # background_image_path = "images/background.jpg"
# # # background_base64 = get_base64_of_bin_file(background_image_path)

# # # # ------------------ CUSTOM CSS ------------------
# # # st.markdown(f"""
# # #     <style>
# # #     [data-testid="stAppViewContainer"] {{
# # #         background-image: url("data:image/jpg;base64,{background_base64}");
# # #         background-size: cover;
# # #         background-position: center;
# # #         background-repeat: no-repeat;
# # #     }}
# # #     .box {{
# # #         background-color: rgba(255, 255, 255, 0.8);
# # #         padding: 20px 25px;
# # #         border-radius: 15px;
# # #         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
# # #         margin-bottom: 20px;
# # #         color: #000000;
# # #     }}
# # #     .subheader {{
# # #         font-size: 1.4rem;
# # #         font-weight: 600;
# # #         color: #222;
# # #         background-color: rgba(240, 240, 240, 0.8);
# # #         border-radius: 12px;
# # #         padding: 10px 15px;
# # #         text-align: center;
# # #         margin-bottom: 15px;
# # #         box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
# # #     }}
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # ------------------ LAYOUT ------------------
# # # col1, col2 = st.columns(2)

# # # with col1:
# # #     st.markdown('<div class="subheader">🚴 VR Cycling ...</div>', unsafe_allow_html=True)

# # #     paragraph_en = """This is a sample paragraph in English. 
# # #     It represents the same content translated into different languages."""
# # #     paragraph_si = """මෙය ඉංග්‍රීසි පාඨයේ සිංහල පරිවර්තනයකි. 
# # #     එකම අන්තර්ගතය විවිධ භාෂාවලින් නිරූපණය කරයි."""
# # #     paragraph_ta = """இது ஆங்கில பத்தி தமிழ் மொழிபெயர்ப்பு ஆகும். 
# # #     அதே உள்ளடக்கத்தை வேறு மொழிகளில் வெளிப்படுத்துகிறது."""

# # #     st.markdown(f'<div class="box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
# # #     st.markdown(f'<div class="box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
# # #     st.markdown(f'<div class="box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# # # with col2:
# # #     st.markdown('<div class="subheader">About This Section</div>', unsafe_allow_html=True)
# # #     st.markdown(
# # #         '<div class="box">This section displays some text at the top and dynamic MQTT visual below it.</div>',
# # #         unsafe_allow_html=True
# # #     )

# # #     st.markdown('<div class="subheader">Live MQTT Path</div>', unsafe_allow_html=True)
# # #     plot_placeholder = st.empty()

# # # # ------------------ LOAD PATH DATA ------------------
# # # try:
# # #     path_data = np.loadtxt("GregoryPathData.txt", delimiter=",")  # lat,long per line
# # #     lats, longs = path_data[:, 0], path_data[:, 1]

# # #     # Normalize to fit visually
# # #     lats = (lats - np.min(lats)) / (np.max(lats) - np.min(lats))
# # #     longs = (longs - np.min(longs)) / (np.max(longs) - np.min(longs))

# # #     # Interpolate to 302 points (0–301)
# # #     indices = np.linspace(0, len(lats) - 1, 302)
# # #     interp_lats = np.interp(indices, np.arange(len(lats)), lats)
# # #     interp_longs = np.interp(indices, np.arange(len(longs)), longs)

# # # except Exception as e:
# # #     st.error(f"Error loading GregoryPathData.txt: {e}")
# # #     st.stop()

# # # # ------------------ FUNCTION TO DRAW PATH ------------------
# # # def plot_path(h_value, g_value):
# # #     fig = go.Figure()

# # #     # Draw the path
# # #     fig.add_trace(go.Scatter(
# # #         x=interp_longs,
# # #         y=interp_lats,
# # #         mode="lines",
# # #         line=dict(color="gray", width=4),
# # #         name="Path"
# # #     ))

# # #     # HIncTime pointer
# # #     fig.add_trace(go.Scatter(
# # #         x=[interp_longs[h_value]],
# # #         y=[interp_lats[h_value]],
# # #         mode="markers",
# # #         marker=dict(color="blue", size=15),
# # #         name="HIncTime"
# # #     ))

# # #     # GIncTime pointer
# # #     fig.add_trace(go.Scatter(
# # #         x=[interp_longs[g_value]],
# # #         y=[interp_lats[g_value]],
# # #         mode="markers",
# # #         marker=dict(color="red", size=15),
# # #         name="GIncTime"
# # #     ))

# # #     fig.update_layout(
# # #         xaxis=dict(visible=False),
# # #         yaxis=dict(visible=False, scaleanchor="x", scaleratio=1),
# # #         showlegend=False,
# # #         margin=dict(l=0, r=0, t=0, b=0),
# # #         height=400,
# # #         plot_bgcolor="rgba(0,0,0,0)",
# # #         paper_bgcolor="rgba(0,0,0,0)"
# # #     )

# # #     return fig

# # # # ------------------ DISPLAY LOOP ------------------
# # # # Refresh every 1000 milliseconds (1 second)
# # # st_autorefresh(interval=1000, key="mqtt_refresh")

# # # # Read latest MQTT data safely
# # # with mqtt_lock:
# # #     h_value = int(np.clip(mqtt_data["HIncTime"], 0, 301))
# # #     g_value = int(np.clip(mqtt_data["GIncTime"], 0, 301))

# # # # Default to start if no values yet
# # # if h_value == 0 and g_value == 0:
# # #     h_value, g_value = 0, 0

# # # # Plot figure
# # # fig = plot_path(h_value, g_value)
# # # plot_placeholder.plotly_chart(fig, use_container_width=True)

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
from streamlit_autorefresh import st_autorefresh

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

# # # ---------- RIGHT COLUMN ----------
# # with col2:
# #     st.markdown('<div class="subheader">📊 Real-time MQTT Visual</div>', unsafe_allow_html=True)
# #     bar_placeholder = st.empty()

# # ---------- NEW RIGHT COLUMN ----------
# # with col2:
# #     st.markdown('<div class="subheader">🗺️ Live Route — Nuwara Eliya</div>', unsafe_allow_html=True)
# #     map_placeholder = st.empty()

# # # ------------------ NEW DISPLAY LOOP ------------------
# # while True:
# #     h_value = mqtt_data["HIncTime"]
# #     g_value = mqtt_data["GIncTime"]

# #     # Clip values safely
# #     h_idx = max(0, min(h_value, len(path_coords)-1))
# #     g_idx = max(0, min(g_value, len(path_coords)-1))

# #     # Get coordinates
# #     h_lat, h_lon = path_coords[h_idx]
# #     g_lat, g_lon = path_coords[g_idx]

# #     # Center map at rider A - feel free to change
# #     m = folium.Map(location=[h_lat, h_lon], zoom_start=17)

# #     # Rider A marker (Blue)
# #     folium.CircleMarker(
# #         location=[h_lat, h_lon],
# #         radius=8,
# #         popup=f"Rider A — {h_idx} / 301",
# #         color="blue",
# #         fill=True,
# #         fill_opacity=0.9
# #     ).add_to(m)

# #     # Rider B marker (Red)
# #     folium.CircleMarker(
# #         location=[g_lat, g_lon],
# #         radius=8,
# #         popup=f"Rider B — {g_idx} / 301",
# #         color="red",
# #         fill=True,
# #         fill_opacity=0.9
# #     ).add_to(m)

# #     # Draw path polyline
# #     folium.PolyLine(path_coords, weight=4).add_to(m)

# #     # Show map
# #     with col2:
# #         map_placeholder = st_folium(m, width=450, height=450)

# #     time.sleep(1)
with col2:
    st.markdown('<div class="subheader">🗺️ Live Route — Nuwara Eliya</div>', unsafe_allow_html=True)
    map_placeholder = st.empty()

# Update map every second
while True:
    h_value = mqtt_data["HIncTime"]
    g_value = mqtt_data["GIncTime"]

    h_idx = max(0, min(h_value, len(path_coords)-1))
    g_idx = max(0, min(g_value, len(path_coords)-1))

    h_lat, h_lon = path_coords[h_idx]
    g_lat, g_lon = path_coords[g_idx]

    m = folium.Map(location=[h_lat, h_lon], zoom_start=17)
    folium.CircleMarker([h_lat, h_lon], radius=8, color="blue", fill=True).add_to(m)
    folium.CircleMarker([g_lat, g_lon], radius=8, color="red", fill=True).add_to(m)
    folium.PolyLine(path_coords, weight=4).add_to(m)

    with map_placeholder:
        if "map_key" not in st.session_state:
            st.session_state.map_key = 0

        st.session_state.map_key += 1

        st_folium(
            m,
            width=450,
            height=450,
            returned_objects=[],
            key=f"map_{st.session_state.map_key}"
        )


    time.sleep(1)

# import streamlit as st
# from PIL import Image
# import base64
# import threading
# import paho.mqtt.client as mqtt
# import time
# import pandas as pd

# # NEW: Leaflet imports
# from streamlit_leaflet import st_leaflet, Map, Marker, Polyline, TileLayer

# # Load path points
# df = pd.read_csv("interpolated_path.csv")
# path_coords = list(zip(df["latitude"], df["longitude"]))  # [(lat, lon), ...]

# # ------------------ PAGE SETTINGS ------------------
# st.set_page_config(layout="wide", page_title="VR Cycling", page_icon="🚴")

# # ------------------ FUNCTIONS ------------------
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # ------------------ MQTT CONFIG ------------------
# BROKER = "18.140.19.253"
# PORT = 8090
# USERNAME = "bikeuser"
# PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
# TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

# mqtt_data = {"HIncTime": 0, "GIncTime": 0}

# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         client.subscribe(TOPICS)

# def on_message(client, userdata, msg):
#     topic = msg.topic
#     payload = msg.payload.decode("utf-8")
#     try:
#         value = int(payload)
#         value = max(0, min(len(path_coords)-1, value))
#         if topic.endswith("HIncTime"):
#             mqtt_data["HIncTime"] = value
#         elif topic.endswith("GIncTime"):
#             mqtt_data["GIncTime"] = value
#     except ValueError:
#         pass

# def mqtt_loop():
#     client = mqtt.Client()
#     client.username_pw_set(USERNAME, PASSWORD)
#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect(BROKER, PORT, 60)
#     client.loop_forever()

# threading.Thread(target=mqtt_loop, daemon=True).start()

# # ------------------ BACKGROUND ------------------
# background_image_path = "images/background.jpg"
# background_base64 = get_base64_of_bin_file(background_image_path)

# st.markdown(f"""
# <style>
#     body {{
#         font-family: 'Segoe UI', sans-serif;
#     }}
#     [data-testid="stAppViewContainer"] {{
#         background-image: url("data:image/jpg;base64,{background_base64}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     .main-title {{
#         font-size: 2.2rem;
#         font-weight: bold;
#         text-align: center;
#         color: #fff;
#         background: rgba(0, 0, 0, 0.55);
#         padding: 15px;
#         border-radius: 12px;
#         box-shadow: 0 4px 10px rgba(0,0,0,0.3);
#         margin-bottom: 25px;
#     }}
#     .content-box {{
#         background-color: rgba(255, 255, 255, 0.85);
#         padding: 25px 30px;
#         border-radius: 20px;
#         box-shadow: 0 6px 15px rgba(0,0,0,0.25);
#         color: #000;
#         margin-bottom: 20px;
#     }}
#     .subheader {{
#         font-size: 1.4rem;
#         font-weight: 600;
#         color: #222;
#         text-align: center;
#         margin-bottom: 15px;
#     }}

#     /* --- Progress bar and pointers --- */
#     .progress-container {{
#         position: relative;
#         width: 95%;
#         margin: 45px auto 30px auto;
#         height: 20px;
#     }}

#     .progress-bar {{
#         position: absolute;
#         top: 50%;
#         left: 0;
#         transform: translateY(-50%);
#         width: 100%;
#         height: 10px;
#         background: linear-gradient(90deg, #ddd, #ccc);
#         border-radius: 5px;
#         overflow: hidden;
#         box-shadow: inset 0 2px 6px rgba(0,0,0,0.2);
#     }}

#     .pointer {{
#         position: absolute;
#         top: 50%;
#         transform: translate(-50%, -50%);
#         width: 22px;
#         height: 22px;
#         border-radius: 50%;
#         background-color: #3498db;
#         transition: left 0.5s ease-in-out;
#         box-shadow: 0 0 10px rgba(0,0,0,0.4);
#         border: 3px solid white;
#         z-index: 10;
#     }}
#     .pointer2 {{
#         background-color: #e74c3c;
#         z-index: 11;
#     }}

#     .value-box {{
#         text-align: center;
#         font-weight: 600;
#         font-size: 1.1rem;
#         color: #333;
#         background: rgba(255,255,255,0.8);
#         border-radius: 10px;
#         padding: 10px;
#         display: inline-block;
#         margin-top: 5px;
#         box-shadow: 0 3px 6px rgba(0,0,0,0.2);
#     }}
# </style>
# """, unsafe_allow_html=True)

# # ------------------ PAGE TITLE ------------------
# st.markdown('<div class="main-title">🚴 VR Cycling — Live Tracking Dashboard</div>', unsafe_allow_html=True)

# # ------------------ LAYOUT ------------------
# col1, col2 = st.columns([1,1])

# # ---------- LEFT COLUMN ----------
# with col1:
#     st.markdown('<div class="subheader">🌍 Multilingual Description</div>', unsafe_allow_html=True)

#     paragraph_en = "This VR cycling dashboard allows you to track live MQTT data and view progress in real time."
#     paragraph_si = "මෙම VR බයිසිකල් ඩැෂ්බෝර්ඩ් මගින් ඔබට සජීවී MQTT දත්ත නිරීක්ෂණය කළ හැක."
#     paragraph_ta = "இந்த VR சைக்கிளிங் டாஷ்போர்ட் வழியாக நேரடி MQTT தரவை கண்காணிக்க முடியும்."

#     st.markdown(f'<div class="content-box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="content-box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="content-box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# # ---------- RIGHT COLUMN ----------
# with col2:
#     st.markdown('<div class="subheader">🗺️ Live Route — Nuwara Eliya</div>', unsafe_allow_html=True)

# # Initialize map once
# start_lat, start_lon = path_coords[0]

# if "leaf_map" not in st.session_state:
#     m = Map(center=[start_lat, start_lon], zoom=17)
#     TileLayer().add_to(m)
    
#     # Polyline route
#     Polyline(locations=path_coords, weight=4).add_to(m)

#     # Rider markers
#     markerA = Marker(location=[start_lat, start_lon])
#     markerB = Marker(location=[start_lat, start_lon])
#     markerA.add_to(m)
#     markerB.add_to(m)

#     st.session_state.leaf_map = m
#     st.session_state.markerA = markerA
#     st.session_state.markerB = markerB

# map_holder = st.empty()

# # Live update loop
# while True:
#     h_idx = mqtt_data["HIncTime"]
#     g_idx = mqtt_data["GIncTime"]

#     h_lat, h_lon = path_coords[h_idx]
#     g_lat, g_lon = path_coords[g_idx]

#     # Update ONLY marker positions
#     st.session_state.markerA.location = [h_lat, h_lon]
#     st.session_state.markerB.location = [g_lat, g_lon]

#     map_holder.write(
#         st_leaflet(st.session_state.leaf_map, key="live_map")
#     )

#     time.sleep(0.3)
