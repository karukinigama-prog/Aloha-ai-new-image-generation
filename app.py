import streamlit as st
import random
import urllib.parse

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Alpha AI Elite | Image Engine",
    page_icon="🤖",
    layout="centered"
)

# --- PREMIUM DARK UI CUSTOMIZATION ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0a0a;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #00ffcc !important;
        border: 1px solid #333 !important;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        box-shadow: 0px 0px 15px #00ffcc;
        color: white;
    }
    footer {visibility: hidden;}
    .custom-footer {
        text-align: center;
        padding: 20px;
        color: #555;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🤖 Alpha AI Elite")
st.subheader("High-Speed Imagination Mode")
st.write("Created by **Hasith Heshan**")
st.write("---")

# --- USER INPUT ---
user_prompt = st.text_input("Enter your imagination:", placeholder="e.g. A futuristic Iron Man suit, 8k, cinematic...")

# Settings in columns
col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Style", ["Natural", "Cyberpunk", "Anime", "Realistic", "3D Render"])
with col2:
    aspect = st.selectbox("Aspect Ratio", ["Square (1:1)", "Widescreen (16:9)", "Portrait (9:16)"])

# Process logic
if st.button("GENERATE IMAGE 🚀"):
    if user_prompt:
        with st.spinner("Alpha AI is visualizing..."):
            # 1. Clean the prompt for URL (Handle spaces/special chars)
            full_prompt = f"{user_prompt}, {style} style, high quality"
            encoded_prompt = urllib.parse.quote(full_prompt)
            
            # 2. Generate unique seed to avoid cached results
            seed = random.randint(1, 9999999)
            
            # 3. Handle Dimensions
            width, height = 1024, 1024
            if "16:9" in aspect: height = 576
            if "9:16" in aspect: width = 576
            
            # 4. Create the final URL
            # We use nologo=true for a professional look
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed={seed}&width={width}&height={height}&nologo=true"
            
            # 5. Display the image
            # Loading directly via URL is much faster than downloading to server first
            st.image(image_url, caption=f"Generated: {user_prompt}", use_container_width=True)
            
            # 6. Provide direct link for manual saving
            st.success("Generation Complete!")
            st.markdown(f"[🔗 Open Direct Image Link]({image_url})")
            st.info("Tip: Right-click the image and select 'Save Image As' to download to your PC.")
    else:
        st.warning("Please type something first!")

# --- FOOTER ---
st.markdown("""
    <div class="custom-footer">
        Alpha AI Project | Created by Hasith Heshan | Bandarawela Central College
    </div>
    """, unsafe_allow_html=True)
