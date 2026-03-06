"""
MULTIMODAL ADVANCED RAG GITHUB REPOSITORY CHATBOT
==================================================
Home Page / Landing Page

This application implements a production-grade Retrieval-Augmented Generation (RAG)
system for analyzing GitHub repositories using AI.

Author: RabbitAI Project
Date: March 2026
"""

import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="Advanced RAG GitHub Chatbot - Home",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state for shared data across pages
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "repo_processed" not in st.session_state:
    st.session_state.repo_processed = False

if "repo_stats" not in st.session_state:
    st.session_state.repo_stats = None

# Custom CSS
st.markdown(
    """
<style>
    .hero-section {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .feature-card {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #667eea;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .tech-badge {
        display: inline-block;
        background-color: #667eea;
        color: white;
        padding: 6px 14px;
        margin: 5px;
        border-radius: 15px;
        font-size: 14px;
    }
    .cta-button {
        background-color: #28a745;
        color: white;
        padding: 15px 30px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
<div class="hero-section">
    <h1>🤖 Advanced RAG GitHub Repository Chatbot</h1>
    <p style="font-size: 20px; margin-top: 15px;">
        Understand any codebase through natural language conversations
    </p>
    <p style="font-size: 16px; opacity: 0.9;">
        Powered by Google Gemini, ChromaDB, and state-of-the-art RAG technology
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# Navigation Buttons
st.markdown("### 🚀 Get Started")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
    <div class="feature-card">
        <h3>💬 Chatbot</h3>
        <p>Process repositories and ask questions about the code</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("Go to Chatbot ➡️", use_container_width=True, type="primary"):
        st.switch_page("pages/3_💬_Chatbot.py")

with col2:
    st.markdown(
        """
    <div class="feature-card">
        <h3>📊 Repository Stats</h3>
        <p>View detailed analytics about processed repositories</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("View Stats ➡️", use_container_width=True):
        st.switch_page("pages/1_📊_Repository_Stats.py")

with col3:
    st.markdown(
        """
    <div class="feature-card">
        <h3>📚 How to Use</h3>
        <p>Complete guide with examples and tips</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("Learn More ➡️", use_container_width=True):
        st.switch_page("pages/2_📚_How_to_Use.py")

st.markdown("---")

# What is RAG Section
st.header("🧠 What is RAG?")
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
    **Retrieval-Augmented Generation (RAG)** combines the power of search and AI to provide 
    accurate, source-based answers.
    
    Traditional chatbots can hallucinate or provide outdated information. RAG solves this by:
    
    1. **📥 Ingesting** your codebase into a vector database
    2. **🔍 Retrieving** relevant code snippets for each question
    3. **🤖 Generating** answers grounded in actual code
    4. **💬 Remembering** conversation context for follow-ups
    """
    )

with col2:
    st.markdown(
        """
    ### How It Works:
    
    ```
    Your Question
         ↓
    [Vector Embedding]
         ↓
    [Similarity Search in ChromaDB]
         ↓
    [Retrieve Top 6 Code Chunks]
         ↓
    [Send to LLaMA 3 with Context]
         ↓
    ✨ AI-Generated Answer ✨
    ```
    
    **Result:** Accurate answers backed by real code!
    """
    )

st.markdown("---")

# Key Features
st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    ### 🎯 Intelligent Code Understanding
    - **Semantic Search**: Finds relevant code based on meaning, not just keywords
    - **Multi-Language Support**: JavaScript, Python, TypeScript, and more
    - **Context-Aware**: Maintains conversation history for follow-up questions
    
    ### ⚡ Blazing Fast Performance
    - **Groq LPU**: 10x faster than traditional GPU inference
    - **Efficient Embeddings**: 384-dim vectors for quick similarity search
    - **HNSW Indexing**: O(log n) retrieval time with ChromaDB
    """
    )

with col2:
    st.markdown(
        """
    ### 🔒 Accurate & Reliable
    - **Source Attribution**: Always references specific files
    - **No Hallucination**: Answers only from your codebase
    - **Transparent**: View retrieved code chunks for verification
    
    ### 🎨 User-Friendly Interface
    - **Dynamic Processing**: Load any public GitHub repo
    - **Clean Chat UI**: Natural conversation experience
    - **Detailed Stats**: View comprehensive repository analytics
    """
    )

st.markdown("---")

# Technology Stack
st.header("🛠️ Technology Stack")

st.markdown(
    """
This application is built with cutting-edge AI and database technologies:
"""
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**Frontend**")
    st.markdown('<span class="tech-badge">Streamlit</span>', unsafe_allow_html=True)
    st.markdown('<span class="tech-badge">Python</span>', unsafe_allow_html=True)

with col2:
    st.markdown("**AI Models**")
    st.markdown('<span class="tech-badge">LLaMA 3.1-8B</span>', unsafe_allow_html=True)
    st.markdown('<span class="tech-badge">MiniLM-L6-v2</span>', unsafe_allow_html=True)

with col3:
    st.markdown("**Infrastructure**")
    st.markdown('<span class="tech-badge">Groq LPU</span>', unsafe_allow_html=True)
    st.markdown('<span class="tech-badge">ChromaDB</span>', unsafe_allow_html=True)

with col4:
    st.markdown("**Framework**")
    st.markdown('<span class="tech-badge">LangChain</span>', unsafe_allow_html=True)
    st.markdown('<span class="tech-badge">HuggingFace</span>', unsafe_allow_html=True)

st.markdown("---")

# Use Cases
st.header("💼 Use Cases")

use_cases = [
    ("🎓", "**Learning New Codebases**", "Quickly understand unfamiliar projects"),
    ("🔍", "**Code Review**", "Analyze architecture and design patterns"),
    ("📚", "**Documentation**", "Generate insights about code structure"),
    ("🐛", "**Debugging**", "Understand how different parts interact"),
    ("🚀", "**Onboarding**", "Help new team members get up to speed"),
    ("🔬", "**Research**", "Study open-source implementations"),
]

cols = st.columns(3)
for i, (icon, title, description) in enumerate(use_cases):
    with cols[i % 3]:
        st.markdown(
            f"""
        <div class="feature-card">
            <h3>{icon} {title}</h3>
            <p>{description}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# Quick Start CTA
st.header("🚀 Ready to Explore Code?")

st.info(
    """
**Get started in 3 simple steps:**
1. Navigate to the **💬 Chatbot** page
2. Enter any public GitHub repository URL
3. Wait for processing, then ask questions!
"""
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎯 Start Chatting Now!", use_container_width=True, type="primary"):
        st.switch_page("pages/3_💬_Chatbot.py")

st.markdown("---")

# Current Status
if st.session_state.repo_processed and st.session_state.repo_stats:
    st.success("✅ A repository is currently loaded and ready for questions!")
    stats = st.session_state.repo_stats

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Repository", stats.get("repo_name", "Unknown"))
    with col2:
        st.metric("Total Files", stats.get("total_files", 0))
    with col3:
        st.metric("Code Chunks", stats.get("total_chunks", 0))
    with col4:
        if st.button("View Details ➡️"):
            st.switch_page("pages/1_📊_Repository_Stats.py")
else:
    st.info("ℹ️ No repository loaded yet. Visit the Chatbot page to process one!")

# Footer
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; color: #666; padding: 20px;">
    <p><b>Advanced RAG GitHub Repository Chatbot</b></p>
    <p>Built with ❤️ by RabbitAI Project • March 2026</p>
    <p style="font-size: 12px;">Powered by Groq LLaMA 3.1-8B-Instant, ChromaDB, LangChain & Streamlit</p>
</div>
""",
    unsafe_allow_html=True,
)
