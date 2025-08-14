import streamlit as st
from PIL import Image
import requests

st.set_page_config(page_title="App Samples", page_icon="✨")

st.title("✨ App Samples")
st.markdown("Here are a couple of examples of what this app can generate for you!")

# --- Sample Data ---
sample_data = {
    "Vintage Leather Backpack": {
        "image_path": "pages/bag1.png",
        "notes": "Handcrafted from full-grain leather. Features multiple compartments and adjustable straps. Perfect for daily use or travel.",
        "metric_label": "Capacity",
        "metric_value": "20 Liters",
        "copy": """
        ### 1. Product Title:
        **The Journeyman: Handcrafted Vintage Leather Backpack**

        ### 2. Product Description:
        Discover the perfect blend of timeless style and rugged functionality with The Journeyman Backpack. Handcrafted from premium full-grain leather, this backpack is built to last and develops a unique patina over time.

        *   **Spacious Main Compartment:** Ample room for your laptop, books, and daily essentials.
        *   **Multiple Pockets:** Keep your gear organized with a front zippered pocket and two side pockets.
        *   **Comfortable & Adjustable:** Padded, adjustable shoulder straps ensure a comfortable fit for all-day wear.
        *   **Durable Construction:** Reinforced stitching and high-quality brass hardware.

        ### 3. Social Media Posts:
        **Instagram:**
        Adventure awaits with The Journeyman Backpack. 🎒 Handcrafted, durable, and stylish—it's the last backpack you'll ever need. #VintageBackpack #LeatherGoods #Handcrafted #TravelGear #EverydayCarry

        **Facebook:**
        Tired of backpacks that fall apart? The Journeyman is crafted from 100% full-grain leather to withstand your daily adventures. Click to shop now! #LeatherBackpack #DurableGoods #VintageStyle #ShopNow

        ### 4. SEO Keywords:
        vintage leather backpack, handcrafted backpack, full-grain leather bag, durable travel backpack, men's leather rucksack
        """
    },
    
    "Smartwatch": {
        "image_url": "https://images.unsplash.com/photo-1544117519-31a4b719223d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "notes": "Fitness tracking (heart rate, steps), long battery life (14 days), waterproof, customizable watch faces.",
        "metric_label": "Battery Life",
        "metric_value": "14 Days",
        "copy": """
        ### 1. Product Title:
        **The Apex: Your Ultimate Smartwatch for Fitness & Life**

        ### 2. Product Description:
        Meet The Apex, the smartwatch that keeps up with your life. With advanced fitness tracking and a battery that just won't quit, you can focus on your goals without interruption.

        *   **24/7 Health Monitoring:** Track your heart rate, steps, sleep patterns, and more.
        *   **14-Day Battery Life:** Spend more time moving and less time charging.
        *   **Waterproof Design:** From swimming laps to running in the rain, The Apex is ready for anything.
        *   **Customizable Faces:** Match your watch to your style with hundreds of customizable faces.

        ### 3. Social Media Posts:
        **Instagram:**
        Level up your fitness game with The Apex Smartwatch. ⌚ 14-day battery life means it's always ready when you are. #Smartwatch #FitnessTracker #TechGadgets #WorkoutMotivation #HealthyLifestyle

        **Facebook:**
        The Apex Smartwatch combines cutting-edge tech with a sleek design. Track your fitness, stay connected, and do it all in style. Learn more and order yours today! #Smartwatch #WearableTech #FitnessGoals #Tech

        ### 4. SEO Keywords:
        smartwatch, fitness tracker, waterproof watch, long battery smartwatch, health tracker watch
        """
    }
}

# --- Create Tabs ---
tab1_title, tab2_title = sample_data.keys()
tab1, tab2 = st.tabs([f"🎒 {tab1_title}", f"⌚ {tab2_title}"])

# --- Populate Tab 1 ---
with tab1:
    sample = sample_data[tab1_title]
    with st.container(border=True):
        col1, col2 = st.columns([0.4, 0.6])
        with col1:
            st.subheader(tab1_title)
            image = Image.open(sample["image_path"])
            st.image(image)
            st.metric(label=sample["metric_label"], value=sample["metric_value"])
            st.info(f"**Notes:** {sample['notes']}")
        with col2:
            st.markdown(sample["copy"])

# --- Populate Tab 2 ---
with tab2:
    sample = sample_data[tab2_title]
    with st.container(border=True):
        col1, col2 = st.columns([0.4, 0.6])
        with col1:
            st.subheader(tab2_title)
            try:
                image = Image.open(requests.get(sample["image_url"], stream=True).raw)
                st.image(image)
                st.metric(label=sample["metric_label"], value=sample["metric_value"])
            except Exception as e:
                st.error(f"Could not load image. {e}")
            st.info(f"**Notes:** {sample['notes']}")
        with col2:
            st.markdown(sample["copy"])