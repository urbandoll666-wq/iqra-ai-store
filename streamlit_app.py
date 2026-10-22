import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Iqra Mazhar - AI App Store",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #64748B;
        margin-bottom: 30px;
    }
    .app-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section with Branding
st.markdown("<h1 class='main-title'>🤖 Iqra Mazhar AI App Store</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Your One-Stop Hub for Custom AI Tools & Automation Solutions</p>", unsafe_allow_html=True)

st.divider()

# Search and Filter
col1, col2 = st.columns([3, 1])
with col1:
    search_query = st.text_input("🔍 Search AI Tools...", placeholder="Type tool name or keyword...")
with col2:
    category = st.selectbox("📁 Category", ["All Categories", "Content Creation", "Visuals & Design", "Data & Research", "Utilities"])

st.markdown("### 🌟 Featured AI Tools")

# Sample App Cards
apps = [
    {
        "title": "🎬 AI Script Generator",
        "category": "Content Creation",
        "desc": "Generate high-engaging video scripts for YouTube and Social Media in seconds.",
        "icon": "📝"
    },
    {
        "title": "🎨 AI Visual Asset Prompt Craft",
        "category": "Visuals & Design",
        "desc": "Create perfect image generation prompts for Midjourney, DALL-E, and Leonardo AI.",
        "icon": "🖼️"
    },
    {
        "title": "📊 Science & History Research Assistant",
        "category": "Data & Research",
        "desc": "Synthesize scientific papers and historical data into concise video concepts.",
        "icon": "🔬"
    },
    {
        "title": "🚀 YouTube Analytics Predictor",
        "category": "Utilities",
        "desc": "Analyze views per hour and retention performance metrics for videos.",
        "icon": "📈"
    }
]

# Display Cards in Grid
cols = st.columns(2)
for idx, app in enumerate(apps):
    if category == "All Categories" or app["category"] == category:
        if not search_query or search_query.lower() in app["title"].lower() or search_query.lower() in app["desc"].lower():
            with cols[idx % 2]:
                with st.container():
                    st.markdown(f"""
                    <div class='app-card'>
                        <h3>{app['icon']} {app['title']}</h3>
                        <p><b>Category:</b> {app['category']}</p>
                        <p>{app['desc']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Launch {app['title']}", key=f"btn_{idx}"):
                        st.info(f"Opening {app['title']}... (API Configured)")

st.divider()

# Footer
st.markdown("""
    <div style='text-align: center; color: #94A3B8; font-size: 0.9rem;'>
        Powered by Google AI Studio | Designed & Managed by <b>Iqra Mazhar</b>
    </div>
""", unsafe_allow_html=True)