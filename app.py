import streamlit as st
import requests
import random
from urllib.parse import quote

# Page Setup
st.set_page_config(
    page_title="AI Image Creator Studio",
    page_icon="🎨"
)

# Title
st.title("🎨 AI Image Creator Studio")
st.write("Create amazing AI-generated images with different art styles.")

# Prompt Input
user_input = st.text_input(
    "Describe your masterpiece",
    placeholder="Example: A yellow cat playing football"
)

# Sidebar
st.sidebar.title("⚙️ Generate Settings")

art_style = st.sidebar.selectbox(
    "Select Art Style",
    [
        "Photorealistic",
        "3D Render",
        "Pixel Style",
        "Ghibli",
        "Sketch",
        "Manga",
        "Anime",
        "Cartoon"
    ]
)

# Assignment Task 3
magic_enhancer = st.sidebar.checkbox("✨ Enable Magic Enhance")

# Assignment Task 1
width = st.sidebar.slider(
    "Image Width",
    min_value=256,
    max_value=1024,
    value=512,
    step=16
)

height = st.sidebar.slider(
    "Image Height",
    min_value=256,
    max_value=1024,
    value=512,
    step=16
)

# Art Style Mapping
style_map = {
    "Photorealistic": "photorealistic, DSLR photo, ultra realistic, professional photography",
    "3D Render": "3d render, blender render, octane render, cinematic lighting",
    "Pixel Style": "pixel art, retro game graphics, 8-bit style",
    "Ghibli": "studio ghibli style, hayao miyazaki artwork, anime background art",
    "Sketch": "pencil sketch, black and white drawing, hand drawn sketch, graphite art",
    "Manga": "manga illustration, manga panel style, black and white manga",
    "Anime": "anime style, japanese anime artwork, vibrant anime colors",
    "Cartoon": "cartoon style, disney cartoon illustration, colorful cartoon art"
}

# Assignment Task 4
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A majestic dragon guarding a glowing neon castle",
    "An ancient library floating among the clouds with magical books",
    "A futuristic city where trees are made of glowing glass shards"
]

# Buttons
col1, col2 = st.columns(2)

with col1:
    generate_button = st.button("🎨 Generate Image")

with col2:
    surprise_button = st.button("🎲 Surprise Me!")

active_prompt = None

# Generate Button
if generate_button:

    if user_input.strip() == "":
        st.warning("Please enter a prompt first.")
    else:
        active_prompt = user_input

# Surprise Button
if surprise_button:

    active_prompt = random.choice(surprise_prompts)

    st.info(f"🎲 Surprise Prompt: {active_prompt}")

# Image Generation
if active_prompt:

    with st.spinner("🎨 Generating image... Please wait"):

        full_prompt = (
            f"{active_prompt}, {style_map[art_style]}"
        )

        # Magic Enhance
        if magic_enhancer:
            full_prompt += (
                ", masterpiece, 8k resolution, highly detailed, "
                "trending on artstation, unreal engine 5 render"
            )

        encoded_prompt = quote(full_prompt)

        # Assignment Task 1
        url = (
            f"https://image.pollinations.ai/prompt/"
            f"{encoded_prompt}"
            f"?width={width}&height={height}"
        )

        # Show Image
        st.image(
            url,
            caption=f"{active_prompt} ({art_style})",
            use_container_width=True
        )

        st.success("✅ Image Generated Successfully!")

        st.write(f"**Art Style:** {art_style}")
        st.write(f"**Resolution:** {width} × {height}")

        # Assignment Task 2
        try:
            response = requests.get(url, timeout=60)

            if response.status_code == 200:

                file_name = (
                    f"{art_style.lower().replace(' ', '_')}_image.png"
                )

                st.download_button(
                    label="⬇️ Download Image",
                    data=response.content,
                    file_name=file_name,
                    mime="image/png"
                )

        except:
            st.warning(
                "Image generated successfully, but download is temporarily unavailable."
            )

st.markdown("---")
st.caption(
    "Built for MirAI School of Technology - Virtual Summer Internship 2026"
)