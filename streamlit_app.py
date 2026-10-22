import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Iqra Mazhar - AI Portal",
    page_icon="🔮",
    layout="wide"
)

# Custom Styling (Royal Purple & Pearl White Gradient Look)
st.markdown("""
    <style>
    /* Main Background & Gradient Header */
    .main {
        background: linear-gradient(135deg, #f8f9ff 0%, #f1edff 100%);
    }
    .top-banner {
        background: linear-gradient(90deg, #6b21a8 0%, #9333ea 50%, #c084fc 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(147, 51, 234, 0.25);
        margin-bottom: 25px;
    }
    .title-text {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4c1d95 0%, #7e22ce 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-text {
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .app-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid #e9d5ff;
        box-shadow: 0 10px 25px -5px rgba(126, 34, 206, 0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 15px;
    }
    .app-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px -5px rgba(126, 34, 206, 0.15);
        border-color: #c084fc;
    }
    .badge {
        background: #f3e8ff;
        color: #7e22ce;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Top Announcement Banner
st.markdown("""
    <div class="top-banner">
        ⚡ IQRA MAZHAR AI LABS & AUTOMATION PORTAL &nbsp;•&nbsp; ✉️ Contact: iqrach998@gmail.com
    </div>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='title-text'>🔮 Iqra Mazhar AI Automation Store</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>High-Performance Custom AI Workflows, Prompt Engines & Content Automation Suite</p>", unsafe_allow_html=True)

st.divider()

# Search and Filters
col1, col2 = st.columns([3, 1])
with col1:
    search_query = st.text_input("🔍 Search Workflows & AI Tools...", placeholder="Type keyword (e.g., Script, Prompts, Analytics)...")
with col2:
    category = st.selectbox("📁 Select Category", ["All Categories", "Content Creation", "Visuals & Design", "Data & Research", "Utilities"])

st.markdown("### 🌟 Featured AI Automation Tools")

# AI Tools List
apps = [
    {
        "title": "🎬 AI Script Generator Pro",
        "category": "Content Creation",
        "desc": "Generate high-engaging viral video scripts for YouTube, TikTok, and educational content.",
        "icon": "📝"
    },
    {
        "title": "🎨 Visual Prompt Engineer",
        "category": "Visuals & Design",
        "desc": "Craft hyper-realistic image prompts for Midjourney, DALL-E, and Leonardo AI automatically.",
        "icon": "🖼️"
    },
    {
        "title": "🔬 Science & History Research Assistant",
        "category": "Data & Research",
        "desc": "Synthesize complex scientific publications and historic timelines into fast video concepts.",
        "icon": "⚡"
    },
    {
        "title": "📈 YouTube Analytics Predictor",
        "category": "Utilities",
        "desc": "Analyze Views Per Hour (VPH) multipliers and audience retention curve metrics.",
        "icon": "📊"
    },
    {
        "title": "🎞️ CapCut Scene Organizer",
        "category": "Content Creation",
        "desc": "Automate timeline scene planning and export setups for 1080p 30fps rendering.",
        "icon": "🎥"
    },
    {
        "title": "🗣️ Neural Voice & TTS Suite",
        "category": "Utilities",
        "desc": "Convert text into ultra-realistic natural AI voiceovers for storytelling videos.",
        "icon": "🎙️"
    }
]

# Grid Layout Display
cols = st.columns(2)
for idx, app in enumerate(apps):
    if category == "All Categories" or app["category"] == category:
        if not search_query or search_query.lower() in app["title"].lower() or search_query.lower() in app["desc"].lower():
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="app-card">
                    <div style="display:flex; justify-shadow:space-between; align-items:center; margin-bottom:10px;">
                        <h3 style="margin:0; color:#4c1d95;">{app['icon']} {app['title']}</h3>
                    </div>
                    <span class="badge">{app['category']}</span>
                    <p style="color:#4b5563; margin-top:12px; font-size:0.95rem;">{app['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🚀 Launch {app['title']}", key=f"btn_{idx}"):
                    st.success(f"Launching {app['title']} Engine...")

st.divider()

# Footer
st.markdown("""
    <div style='text-align: center; color: #71717a; font-size: 0.9rem; padding: 10px;'>
        Built & Maintained by <b>Iqra Mazhar</b> | Powered by Custom AI Workflows
    </div>
""", unsafe_allow_html=True)