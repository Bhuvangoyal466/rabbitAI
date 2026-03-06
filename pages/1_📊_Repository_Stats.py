"""
Repository Statistics Page
===========================
Displays detailed statistics about the processed GitHub repository including:
- Total files and code chunks
- Technology stack (complete, scrollable list)
- Images processed
- Additional metadata
"""

import streamlit as st
from ingest import get_repo_stats
import os

# Page Configuration
st.set_page_config(page_title="Repository Stats", page_icon="📊", layout="wide")

# Custom CSS for better visibility
st.markdown(
    """
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
    }
    .tech-stack-container {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        max-height: 400px;
        overflow-y: auto;
    }
    .tech-badge {
        display: inline-block;
        background-color: #1f77b4;
        color: white;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Title
st.title("📊 Repository Statistics")
st.markdown("---")

# Check if repository has been processed
if not st.session_state.get("repo_processed", False):
    st.warning("⚠️ No repository has been processed yet!")
    st.info("👈 Please go to the **Chatbot** page and process a repository first.")

    # Show helpful image or instructions
    st.markdown(
        """
    ### How to Get Started:
    1. Navigate to the **💬 Chatbot** page using the sidebar
    2. Enter a GitHub repository URL
    3. Click "Process Repository"
    4. Return here to view detailed statistics
    """
    )

elif st.session_state.get("repo_stats"):
    stats = st.session_state.repo_stats

    # Main Metrics in Cards
    st.subheader("📈 Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📁 Total Files",
            value=stats.get("total_files", 0),
            help="Total number of files analyzed in the repository",
        )

    with col2:
        st.metric(
            label="🧩 Code Chunks",
            value=stats.get("total_chunks", 0),
            help="Number of semantic code chunks created for RAG",
        )

    with col3:
        st.metric(
            label="🖼️ Images",
            value=stats.get("images_processed", 0),
            help="Number of images and diagrams processed",
        )

    with col4:
        # Calculate average chunk size if available
        avg_chunk = "N/A"
        if stats.get("total_chunks", 0) > 0 and stats.get("total_files", 0) > 0:
            avg_chunk = f"{stats['total_chunks'] // stats['total_files']}"
        st.metric(
            label="📊 Avg Chunks/File",
            value=avg_chunk,
            help="Average number of chunks per file",
        )

    st.markdown("---")

    # Technology Stack Section with Full Visibility
    st.subheader("💻 Technology Stack")
    st.markdown("All programming languages and file types detected in the repository:")

    # Display tech stack in a scrollable, well-formatted container
    tech_stack = stats.get("languages", "Not available")

    if tech_stack and tech_stack != "Not available":
        # Split by comma and create badges
        languages = [lang.strip() for lang in tech_stack.split(",")]

        # Create a nice display with badges
        st.markdown('<div class="tech-stack-container">', unsafe_allow_html=True)

        # Display in columns for better organization
        cols_per_row = 4
        for i in range(0, len(languages), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, lang in enumerate(languages[i : i + cols_per_row]):
                with cols[j]:
                    st.markdown(
                        f'<div class="tech-badge">{lang}</div>', unsafe_allow_html=True
                    )

        st.markdown("</div>", unsafe_allow_html=True)

        # Also display as expandable text for copy-paste
        with st.expander("📋 View as Text (Click to Copy)"):
            st.code(tech_stack, language=None)
    else:
        st.info("No technology stack information available")

    st.markdown("---")

    # Additional Repository Information
    st.subheader("ℹ️ Additional Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### 📂 Repository Details")
        if "repo_url" in stats:
            st.write(f"**URL:** [{stats['repo_url']}]({stats['repo_url']})")

        if "repo_name" in stats:
            st.write(f"**Name:** `{stats['repo_name']}`")

        if os.path.exists("./chroma_db"):
            st.write(f"**Vector DB:** ChromaDB (Local)")
            st.write(f"**Status:** ✅ Active")

    with col2:
        st.markdown("##### ⚙️ Processing Details")
        st.write(f"**Embedding Model:** all-MiniLM-L6-v2")
        st.write(f"**Embedding Dimensions:** 384")
        st.write(f"**Retrieval Strategy:** Similarity Search (k=6)")
        st.write(f"**LLM:** Groq LLaMA 3.1-8B-Instant")

    st.markdown("---")

    # Visualization Section
    st.subheader("📊 Visual Breakdown")

    col1, col2 = st.columns(2)

    with col1:
        # Simple bar chart for file types if we have that data
        st.markdown("##### File Distribution")
        st.info("Detailed file type breakdown coming soon...")

    with col2:
        st.markdown("##### Processing Summary")
        processing_steps = {
            "Repository Cloned": "✅",
            "Code Analyzed": "✅",
            "Embeddings Generated": "✅",
            "Vector DB Stored": "✅",
            "Ready for Chat": "✅",
        }
        for step, status in processing_steps.items():
            st.write(f"{status} {step}")

    # Refresh button
    st.markdown("---")
    if st.button("🔄 Refresh Statistics", type="secondary", use_container_width=True):
        st.rerun()

else:
    st.error("❌ Repository statistics not available")
    st.info("Please process a repository first from the Chatbot page")

# Footer
st.markdown("---")
st.caption("Statistics are updated each time a new repository is processed.")
