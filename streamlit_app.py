import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Iqra Mazhar AI Studio", page_icon="🎬", layout="wide")

# Custom Styling (Purple & White theme)
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #6c5ce7;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #636e72;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🎬 Sci-Com Script Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Generate captivating scientific and historical video scripts for educational content.</p>', unsafe_allow_html=True)

# API Key Input
api_key = st.text_input("Enter your Google AI Studio API Key", type="password")

# Form Inputs
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Video Topic / Title", placeholder="e.g., What If Nothing Isn't Empty? The Quantum Vacuum")
    content_type = st.selectbox("Content Format", ["YouTube Short (Vertical 9:16 - Under 60s)", "Long-Form YouTube Video"])

with col2:
    tone = st.selectbox("Narrative Tone", ["Engaging & Mysterious", "Educational & Scientific", "Cinematic & Dramatic", "Fast-paced & Viral"])
    language = st.selectbox("Language / Style", ["English", "Urdu / Hindi (Roman)"])

if st.button("Generate Script & Hook", type="primary"):
    if not api_key:
        st.error("Please enter your Google AI Studio API Key first!")
    elif not topic:
        st.warning("Please enter a video topic!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            prompt = f"""
            You are an expert YouTube scriptwriter specializing in viral historical, scientific, and mystery storytelling.
            Create a professional video script based on the following details:
            - Topic: {topic}
            - Format: {content_type}
            - Tone: {tone}
            - Language: {language}
            
            Structure the response clearly with:
            1. **Viral Title Options** (3 catchy headlines)
            2. **The Hook** (First 3-5 seconds punchy opening to stop scrolling)
            3. **Body Script** (Divided into engaging segments with visual/B-roll cues in brackets like [Visual: ...])
            4. **Call to Action (CTA) & Outro**
            """
            
            with st.spinner("Crafting your viral script..."):
                response = model.generate_content(prompt)
                
                st.success("Script Generated Successfully!")
                st.markdown("---")
                st.markdown(response.text)
                
                st.download_button(
                    label="📥 Download Script as Text File",
                    data=response.text,
                    file_name=f"{topic.replace(' ', '_')}_script.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {e}")