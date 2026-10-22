import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Iqra Mazhar - AI Toolkit",
    page_icon="🔮",
    layout="wide"
)

# Custom Styling (Royal Purple & Pearl White Premium Look)
st.markdown("""
    <style>
    /* Main Background & Gradient Header */
    .main {
        background: linear-gradient(135deg, #f8f9ff 0%, #f1edff 100%);
    }
    .top-banner {
        background: linear-gradient(90deg, #5b21b6 0%, #7c3aed 50%, #a855f7 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.25);
        margin-bottom: 25px;
    }
    .title-text {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 100%);
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
        box-shadow: 0 10px 25px -5px rgba(109, 40, 217, 0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 15px;
    }
    .app-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px -5px rgba(109, 40, 217, 0.15);
        border-color: #c084fc;
    }
    .badge {
        background: #f3e8ff;
        color: #6d28d9;
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
        ✨ IQRA MAZHAR • CREATIVE AI STUDIO &nbsp;•&nbsp; ✉️ Contact: iqrach998@gmail.com
    </div>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='title-text'>🔮 Iqra Mazhar AI Studio & Toolkit</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Bespoke Generative AI Workflows, Prompt Engineering & Science Storytelling Tools</p>", unsafe_allow_html=True)

st.divider()

# Search and Filters
col1, col2 = st.columns([3, 1])
with col1:
    search_query = st.text_input("🔍 Search AI Tools...", placeholder="Type keyword (e.g., Script, Prompts, Research)...")
with col2:
    category = st.selectbox("📁 Select Category", ["All Categories", "Video Production", "Prompts & Visuals", "Research & Science", "Analytics"])

st.markdown("### 🌟 Featured Custom AI Tools")

# AI Tools List
apps = [
    {
        "title": "📝 Sci-Com Script Engine",
        "category": "Video Production",
        "desc": "Generate captivating scientific and historical video scripts for educational content.",
        "icon": "🎬"
    },
    {
        "title": "🖼️ Visual Scene Prompt Crafter",
        "category": "Prompts & Visuals",
        "desc": "Design highly accurate Midjourney and Leonardo AI prompts for 2D/3D visual assets.",
        "icon": "🎨"
    },
    {
        "title": "🔬 Quantum & History Knowledge Engine",
        "category": "Research & Science",
        "desc": "Summarize complex scientific papers, physics concepts, and pre-historic timelines.",
        "icon": "⚛️"
    },
    {
        "title": "📈 VPH & Audience Multiplier",
        "category": "Analytics",
        "desc": "Track Views Per Hour metrics and video performance retention indicators.",
        "icon": "📊"
    },
    {
        "title": "🎥 Timeline & Scene Prep Assistant",
        "category": "Video Production",
        "desc": "Organize render settings and video timelines for 1080p 30fps export efficiency.",
        "icon": "🎞️"
    },
    {
        "title": "🎙️ AI Storytelling Voice Studio",
        "category": "Prompts & Visuals",
        "desc": "Create natural narration prompts for documentaries and short video concepts.",
        "icon": "🔊"
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
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <h3 style="margin:0; color:#4c1d95;">{app['icon']} {app['title']}</h3>
                    </div>
                    <span class="badge">{app['category']}</span>
                    <p style="color:#4b5563; margin-top:12px; font-size:0.95rem;">{app['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🚀 Open {app['title']}", key=f"btn_{idx}"):
                    st.success(f"Opening {app['title']}...")

st.divider()

# Footer
st.markdown("""
    <div style='text-align: center; color: #71717a; font-size: 0.9rem; padding: 10px;'>
        Designed & Developed by <b>Iqra Mazhar</b> | Independent AI Project
    </div>
""", unsafe_allow_html=True)