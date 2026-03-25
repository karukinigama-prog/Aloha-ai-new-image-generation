import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import random

# --- AUTHENTICATION & SECRETS ---
# This looks for the key in your Streamlit Cloud "Secrets" panel
try:
    API_KEY = st.secrets["POLLINATIONS_API_KEY"]
except KeyError:
    st.error("Error: 'POLLINATIONS_API_KEY' not found in Streamlit Secrets. Please add it to your app settings.")
    st.stop()

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alpha AI Elite",
    page_icon="🤖",
    layout="wide"
)

# --- PREMIUM DARK UI (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
    }
    .stTextArea textarea {
        background-color: #111 !important;
        color: #00ffcc !important;
        border: 1px solid #333 !important;
        border-radius: 10px;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: #000;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 12px;
        transition: 0.3s ease;
        text-transform: uppercase;
    }
    .stButton > button:hover {
        box-shadow: 0px 0px 20px #00ffcc;
        color: #fff;
    }
    .footer {
        text-align: center;
        padding: 20px;
        color: #444;
        font-size: 14px;
        border-top: 1px solid #222;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🤖 Alpha AI Elite")
st.write("Professional Image Generation Engine")
st.write("Created by **Hasith Heshan** | Bandarawela Central College")
st.write("---")

# --- USER INTERFACE LAYOUT ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    user_prompt = st.text_area(
        "Enter your imagination:",
        placeholder="Example: A realistic robot building a computer in a neon-lit room, 8k resolution, cinematic lighting...",
        height=150
    )

with col2:
    st.subheader("Settings")
    model_style = st.selectbox("Intelligence Mode", ["Flux Schnell", "Cinematic", "Cyberpunk", "Realistic", "Digital Art"])
    aspect_ratio = st.selectbox("Aspect Ratio", ["1:1 (Square)", "16:9 (Widescreen)", "9:16 (Portrait)"])

# --- GENERATION LOGIC ---
if st.button("GENERATE MASTERPIECE 🚀"):
    if user_prompt:
        with st.spinner("Alpha AI is processing your request..."):
            # Prepare Dimensions
            width, height = 1024, 1024
            if aspect_ratio == "16:9 (Widescreen)": height = 576
            elif aspect_ratio == "9:16 (Portrait)": width = 576
            
            # Combine Prompt and Style
            final_prompt = f"{user_prompt}, {model_style} style, masterpiece, high quality"
            seed = random.randint(1, 1000000)
            
            # API Request URL (Using the Flux model from your key)
            url = f"https://image.pollinations.ai/prompt/{final_prompt}?width={width}&height={height}&seed={seed}&model=flux&nologo=true"
            
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }
            
            try:
                response = requests.get(url, headers=headers, timeout=60)
                
                if response.status_code == 200:
                    img_data = Image.open(BytesIO(response.content))
                    st.image(img_data, caption=f"Prompt: {user_prompt}", use_container_width=True)
                    
                    # Provide Download Button
                    buf = BytesIO()
                    img_data.save(buf, format="PNG")
                    st.download_button(
                        label="Download PNG Image 📥",
                        data=buf.getvalue(),
                        file_name=f"alpha_ai_{seed}.png",
                        mime="image/png"
                    )
                else:
                    st.error(f"Server Error: {response.status_code}. Check your API key or connection.")
            
            except Exception as e:
                st.error(f"Connection Failed: {str(e)}")
    else:
        st.warning("Please enter a description first!")

# --- FOOTER ---
st.markdown('<div class="footer">Created by Hasith Heshan | Powered by Alpha AI Engine</div>', unsafe_allow_html=True)
