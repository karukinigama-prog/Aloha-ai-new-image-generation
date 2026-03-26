import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import random
import urllib.parse

# --- AUTHENTICATION ---
# Use Streamlit Secrets (Recommended) or paste directly for testing
try:
    API_KEY = st.secrets["POLLINATIONS_API_KEY"]
except:
    # If secrets are not set, you can paste your sk_ key here to test
    API_KEY = "sk_Z0oEnm05szbphnbZ9ClRCukKV2HyDMH5" 

# --- PAGE SETUP ---
st.set_page_config(page_title="Alpha AI Elite", page_icon="🤖", layout="wide")

# Premium UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .stButton>button { 
        width: 100%; background: linear-gradient(90deg, #00ffcc, #0088ff); 
        color: black; font-weight: bold; border-radius: 8px;
    }
    .footer { text-align: center; padding: 10px; color: #555; border-top: 1px solid #222; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Alpha AI Elite")
st.write(f"Created by **Hasith Heshan** | Bandarawela Central College")
st.write("---")

# --- UI LAYOUT ---
col1, col2 = st.columns([2, 1])

with col1:
    prompt = st.text_area("What's in your mind?", placeholder="Example: A futuristic Iron Man suit, 8k, cinematic lighting...")

with col2:
    model_choice = st.selectbox("Select Model", ["flux", "turbo", "zimage", "p-image"])
    aspect = st.selectbox("Aspect Ratio", ["1:1 (Square)", "16:9 (Widescreen)", "9:16 (Portrait)"])

# --- GENERATION ---
if st.button("GENERATE MASTERPIECE 🚀"):
    if prompt:
        with st.spinner("Alpha AI is communicating with the server..."):
            # Set dimensions
            width, height = 1024, 1024
            if aspect == "16:9 (Widescreen)": height = 576
            elif aspect == "9:16 (Portrait)": width = 576
            
            seed = random.randint(1, 1000000)
            encoded_prompt = urllib.parse.quote(prompt)
            
            # --- NEW URL STRUCTURE ---
            # Using the new 'gen.pollinations.ai' endpoint
            url = f"https://gen.pollinations.ai/image/{encoded_prompt}?width={width}&height={height}&seed={seed}&model={model_choice}"
            
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }
            
            try:
                # Making the request with the API Key
                response = requests.get(url, headers=headers, timeout=60)
                
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=f"Generated: {prompt}", use_container_width=True)
                    
                    # Download button
                    buf = BytesIO()
                    img.save(buf, format="PNG")
                    st.download_button("Download Image 📥", buf.getvalue(), "alpha_ai.png", "image/png")
                
                elif response.status_code == 401:
                    st.error("Authentication Failed! Please check your API Key.")
                elif response.status_code == 402:
                    st.error("Insufficient Pollen! You need more balance.")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter a prompt!")

st.markdown('<div class="footer">Alpha AI Project | Created by Hasith Heshan</div>', unsafe_allow_html=True)
