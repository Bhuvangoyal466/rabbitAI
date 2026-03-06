"""
How to Use Page
===============
Comprehensive guide on using the Advanced RAG GitHub Repository Chatbot.
Includes step-by-step instructions, example questions, and tips.
"""

import streamlit as st

# Page Configuration
st.set_page_config(page_title="How to Use", page_icon="📚", layout="wide")

# Custom CSS for better formatting
st.markdown(
    """
<style>
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
        color: #1f77b4;
    }
    .step-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 15px 0;
    }
    .tip-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    .example-box {
        background-color: #d1ecf1;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #17a2b8;
        margin: 10px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Title
st.title("📚 How to Use the Advanced RAG GitHub Chatbot")
st.markdown(
    "A complete guide to getting the most out of this AI-powered code assistant"
)
st.markdown("---")

# Overview Section
st.header("🎯 What is This?")
st.markdown(
    """
This is a **Retrieval-Augmented Generation (RAG)** chatbot that helps you understand any GitHub repository 
through natural language conversations. It combines:
- 🔍 **Intelligent Code Search** - Finds relevant code snippets using semantic search
- 🤖 **AI Understanding** - Uses LLaMA 3 to explain code in plain English
- 💬 **Conversational Memory** - Remembers context from previous questions
- 🖼️ **Multimodal Support** - Can process code, markdown, and images
"""
)

st.markdown("---")

# Step-by-Step Guide
st.header("🚀 Step-by-Step Guide")

st.markdown("### Step 1: Navigate to the Chatbot Page")
st.markdown(
    """
<div class="step-card">
<b>Action:</b> Click on <b>💬 Chatbot</b> in the sidebar to access the main interface.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("### Step 2: Enter a GitHub Repository URL")
st.markdown(
    """
<div class="step-card">
<b>Action:</b> In the sidebar, paste the full URL of any public GitHub repository.<br><br>
<b>Format:</b> <code>https://github.com/username/repository-name</code><br><br>
<b>Example:</b> <code>https://github.com/facebook/react</code>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("### Step 3: Process the Repository")
st.markdown(
    """
<div class="step-card">
<b>Action:</b> Click the <b>"🚀 Process Repository"</b> button.<br><br>
<b>What happens:</b>
<ul>
    <li>📥 Repository is cloned from GitHub</li>
    <li>🔍 Code is analyzed and chunked intelligently</li>
    <li>📊 Embeddings are generated for semantic search</li>
    <li>💾 Data is stored in ChromaDB vector database</li>
</ul>
<b>Duration:</b> 1-5 minutes depending on repository size
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("### Step 4: Ask Questions!")
st.markdown(
    """
<div class="step-card">
<b>Action:</b> Once processing is complete, type your question in the chat input at the bottom.<br><br>
<b>The AI will:</b>
<ul>
    <li>🔎 Search the codebase for relevant sections</li>
    <li>📖 Read and understand the context</li>
    <li>💡 Generate a clear, technical explanation</li>
    <li>📝 Reference specific files and line numbers</li>
</ul>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("---")

# Example Questions Section
st.header("💡 Example Questions to Ask")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏗️ Architecture & Design")
    st.markdown(
        """
    <div class="example-box">
    <ul>
        <li>"What is the overall architecture of this project?"</li>
        <li>"How is the codebase structured?"</li>
        <li>"What design patterns are being used?"</li>
        <li>"Explain the folder structure"</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🔐 Authentication & Security")
    st.markdown(
        """
    <div class="example-box">
    <ul>
        <li>"How does user authentication work?"</li>
        <li>"Where are API keys stored?"</li>
        <li>"What security measures are implemented?"</li>
        <li>"How is data validation handled?"</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown("### 🎨 Frontend & UI")
    st.markdown(
        """
    <div class="example-box">
    <ul>
        <li>"How does routing work?"</li>
        <li>"What state management approach is used?"</li>
        <li>"Explain the component hierarchy"</li>
        <li>"How are API calls made from the frontend?"</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🗄️ Backend & Database")
    st.markdown(
        """
    <div class="example-box">
    <ul>
        <li>"What database is being used?"</li>
        <li>"How are models/schemas defined?"</li>
        <li>"Explain the API endpoints"</li>
        <li>"How is error handling implemented?"</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Tips and Tricks
st.header("💡 Tips for Best Results")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    <div class="tip-box">
    <b>✅ DO:</b>
    <ul>
        <li>Be specific in your questions</li>
        <li>Ask follow-up questions for clarification</li>
        <li>Reference specific features or components</li>
        <li>Ask about implementation details</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="tip-box">
    <b>❌ DON'T:</b>
    <ul>
        <li>Ask about code outside the repository</li>
        <li>Request to write entirely new features</li>
        <li>Expect real-time code execution</li>
        <li>Ask extremely vague questions</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Technical Details
st.header("⚙️ Technical Details")

tab1, tab2, tab3 = st.tabs(["🤖 AI Models", "🔍 How RAG Works", "💾 Technologies Used"])

with tab1:
    st.markdown(
        """
    ### AI Models Powering This App
    
    **Embedding Model: all-MiniLM-L6-v2**
    - Converts code into 384-dimensional vectors
    - Trained on 1B+ sentence pairs
    - Enables semantic similarity search
    - Fast inference: ~2000 sentences/sec
    
    **Language Model: LLaMA 3.1-8B-Instant (via Groq)**
    - Meta's latest open-source LLM
    - 8,192 token context window
    - 10x faster inference with Groq's LPU hardware
    - Temperature: 0.2 (precise, technical responses)
    """
    )

with tab2:
    st.markdown(
        """
    ### How Retrieval-Augmented Generation Works
    
    **Step 1: Your Question**
    ```
    "How does authentication work?"
    ```
    
    **Step 2: Question is Embedded**
    - Your question is converted to a 384-dim vector
    
    **Step 3: Similarity Search**
    - ChromaDB finds the 6 most similar code chunks
    - Uses HNSW (Hierarchical Navigable Small World) indexing
    - Search time: O(log n)
    
    **Step 4: Context Injection**
    - Retrieved code chunks are added to the prompt
    - Previous chat history is included for context
    
    **Step 5: AI Generation**
    - LLaMA 3 reads the context
    - Generates an answer grounded in actual code
    - References specific files and implementations
    
    **Result: Accurate, Source-Based Answers! ✨**
    """
    )

with tab3:
    st.markdown(
        """
    ### Technology Stack
    
    | Component | Technology | Purpose |
    |-----------|-----------|---------|
    | **Frontend** | Streamlit | Interactive UI framework |
    | **Vector DB** | ChromaDB | Stores code embeddings |
    | **Embeddings** | HuggingFace | Sentence transformers |
    | **LLM** | Groq + LLaMA 3 | Natural language understanding |
    | **Framework** | LangChain | RAG orchestration |
    | **Language** | Python 3.10+ | Core implementation |
    
    **Supported Code Languages:**
    - JavaScript/TypeScript
    - Python
    - HTML/CSS
    - Markdown
    - JSON
    - And many more!
    """
    )

st.markdown("---")

# FAQ Section
st.header("❓ Frequently Asked Questions")

with st.expander("💰 Is this free to use?"):
    st.markdown(
        """
    The application itself is open source and free. However:
    - **Groq API**: Free tier with rate limits (14,400 requests/day)
    - **HuggingFace**: Free for model downloads
    - **ChromaDB**: Free, runs locally
    
    For production use, consider Groq's paid tiers for higher limits.
    """
    )

with st.expander("🔒 Can I use private repositories?"):
    st.markdown(
        """
    Currently, only **public** GitHub repositories are supported. 
    To analyze private repos, you would need to:
    1. Clone the repo manually
    2. Modify the ingestion script to read from local directory
    3. Ensure you have proper authentication
    """
    )

with st.expander("📦 What's the maximum repository size?"):
    st.markdown(
        """
    There's no hard limit, but consider:
    - **Recommended**: < 1000 files for best performance
    - **Large repos (1000-5000 files)**: Slower processing (5-15 mins)
    - **Very large repos (>5000 files)**: May require code to process only specific directories
    
    The embedding generation is the slowest step for large codebases.
    """
    )

with st.expander("🤔 Why is my answer not accurate?"):
    st.markdown(
        """
    Possible reasons:
    1. **Question too vague** - Be more specific
    2. **Code not in retrieved chunks** - Try rephrasing
    3. **Complex logic** - Ask follow-up questions to dig deeper
    4. **LLM limitations** - AI may misinterpret complex code
    
    **Tip**: Check the "View Retrieved Code Chunks" expander to see what code was used.
    """
    )

st.markdown("---")

# Footer
st.success(
    "✅ You're all set! Head over to the **💬 Chatbot** page to start exploring code!"
)

st.markdown("---")
st.caption(
    "💡 Pro Tip: View the Repository Stats page after processing to see detailed analytics!"
)
