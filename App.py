import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alpha AI Elite | Image Generation",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM METALLIC UI CUSTOMIZATION ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #333;
    }
    
    /* Input fields */
    .stTextArea textarea {
        background-color: #121212 !important;
        color: #00ffcc !important;
        border: 1px solid #444 !important;
        border-radius: 10px;
    }

    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(145deg, #1e1e1e, #111111);
        color: #00ffcc;
        border: 1px solid #00ffcc;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background: #00ffcc;
        color: #000;
        box-shadow: 0 0 20px #00ffcc;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #050505;
        color: #666;
        text-align: center;
        padding: 5px;
        font-size: 12px;
        border-top: 1px solid #222;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CORE FUNCTIONS ---
def generate_image(prompt, width=1024, height=1024):
    """Fetches a generated image from the Pollinations API."""
    seed = random.randint(0, 999999)
    # nologo=true removes the watermark for a cleaner look
    url = f"https://image.pollinations.ai/prompt/{prompt}?seed={seed}&width={width}&height={height}&nologo=true"
    
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        return None
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return None

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Alpha AI Elite")
    st.markdown("---")
    st.subheader("Configuration")
    model_type = st.selectbox("Intelligence Mode", ["Imagination (Standard)", "Cinematic", "Cyberpunk", "Realistic"])
    aspect_ratio = st.radio("Aspect Ratio", ["1:1 (Square)", "16:9 (Widescreen)", "9:16 (Portrait)"])
    
    st.markdown("---")
    st.write("Created by **Hasith Heshan**")
    st.write("Project: Alpha AI Elite")

# --- MAIN INTERFACE ---
st.title("🤖 Alpha AI: Imagination Engine")
st.write("Enter a detailed description to generate high-quality AI images instantly.")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    user_input = st.text_area(
        "Describe your vision:",
        placeholder="Example: A futuristic battle-suit standing in a neon city, highly detailed, 8k render, unreal engine 5 style...",
        height=150
    )
    
    # Enhancing the prompt based on selection
    final_prompt = user_input
    if model_type != "Imagination (Standard)":
        final_prompt += f", in {model_type} style, highly detailed masterpiece"

    generate_clicked = st.button("Generate Masterpiece 🚀")

with col2:
    if generate_clicked:
        if user_input:
            with st.spinner("Alpha AI is processing your request..."):
                result_image = generate_image(final_prompt)
                
                if result_image:
                    st.image(result_image, caption="AI Generated Result", use_container_width=True)
                    
                    # Download handling
                    img_byte_arr = BytesIO()
                    result_image.save(img_byte_arr, format='PNG')
                    
                    st.download_button(
                        label="Download PNG 📥",
                        data=img_byte_arr.getvalue(),
                        file_name=f"alpha_ai_{random.randint(100,999)}.png",
                        mime="image/png"
                    )
                else:
                    st.error("Failed to generate image. The server might be busy.")
        else:
            st.warning("Please enter a description first.")

# --- FOOTER ---
st.markdown('<div class="footer">Created by Hasith Heshan | Bandarawela Central College</div>', unsafe_allow_html=True)
