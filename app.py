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
    .stApp { background-color: #050505; color: #ffffff; }
    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #00ffcc !important;
        border: 1px solid #333 !important;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: black; font-weight: bold; border: none;
        border-radius: 5px; padding: 10px; transition: 0.3s;
    }
    .stButton > button:hover { box-shadow: 0px 0px 15px #00ffcc; color: white; }
    footer {visibility: hidden;}
    .custom-footer { text-align: center; padding: 20px; color: #555; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🤖 Alpha AI Elite")
st.subheader("High-Speed Imagination Mode")
st.write("Created by **Hasith Heshan**")
st.write("---")

# --- USER INPUT ---
user_prompt = st.text_input("Enter your imagination:", placeholder="e.g. A futuristic robot in a neon city...")

col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Style", ["Cinematic", "Cyberpunk", "Anime", "Photorealistic", "Digital Art"])
with col2:
    aspect = st.selectbox("Aspect Ratio", ["1:1", "16:9", "9:16"])

if st.button("GENERATE IMAGE 🚀"):
    if user_prompt:
        with st.spinner("Alpha AI is visualizing..."):
            # Clean prompt
            full_prompt = f"{user_prompt}, {style} style, ultra hd, high resolution"
            encoded_prompt = urllib.parse.quote(full_prompt)
            seed = random.randint(1, 100000)
            
            # Setting dimensions
            width, height = 1024, 1024
            if aspect == "16:9": height = 576
            elif aspect == "9:16": width = 576

            # NEW URL STRUCTURE (Public friendly)
            # This uses the direct pollinations renderer which is currently open
            image_url = f"https://pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={seed}&model=flux"
            
            # Display
            st.image(image_url, caption=f"Generated: {user_prompt}", use_container_width=True)
            
            st.success("Generation Complete!")
            st.markdown(f"**[🔗 Open Direct Image Link]({image_url})**")
            st.info("Right-click the image above and 'Save Image As' to download.")
    else:
        st.warning("Please enter a prompt!")

# --- FOOTER ---
st.markdown('<div class="custom-footer">Alpha AI Project | Created by Hasith Heshan | Bandarawela Central College</div>', unsafe_allow_html=True)
