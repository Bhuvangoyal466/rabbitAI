"""
Chatbot Page
============
Main interactive page for processing repositories and asking questions about code.
Includes the full RAG pipeline with conversational memory.
"""

import os
import warnings
import shutil
from pathlib import Path

# CRITICAL: Suppress parallelism warnings from HuggingFace tokenizers
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*torch.*")

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from ingest import process_repository, get_repo_stats, safe_rmtree

# ==============================================================================
# CONFIGURATION
# ==============================================================================

# GOOGLE GEMINI API KEY
# Get your free API key from: https://aistudio.google.com/apikey
<<<<<<< HEAD
# Use Streamlit secrets in production (Streamlit Cloud)
# Use environment variable for local development
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
elif "GOOGLE_API_KEY" not in os.environ:
    # Fallback for local development only
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCE3R_zh2dTrk2ersaInCKn1CYFW6HkFgY"
=======
os.environ["GOOGLE_API_KEY"] = (
    ""  # Replace with your actual Gemini API key
)
>>>>>>> 77f08bb65dffad1daa76e9ce98f1b9a9ec63fec6

# Page Configuration
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# CORE RAG PIPELINE
# ==============================================================================


@st.cache_resource
def load_rag_pipeline():
    """
    Initializes the complete RAG (Retrieval-Augmented Generation) pipeline.
    Cached to avoid reloading on every interaction.
    """

    # Embeddings Model
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    # ChromaDB Vector Store
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

    # Retriever Configuration
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 6}
    )

    # Google Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        max_output_tokens=8192,  # Gemini has much higher token limits
    )

    # Contextualize Question Prompt
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # History-Aware Retriever
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # Main System Prompt
    qa_system_prompt = (
        "You are a Senior Staff Engineer with 10+ years of experience explaining "
        "a codebase to a junior developer. Use the following retrieved code context "
        "to answer questions. Always reference specific file paths when explaining "
        "implementations. If you don't know the answer based on the provided context, "
        "clearly state that. Keep explanations technical but accessible.\n\n"
        "Retrieved Context:\n{context}"
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # Question-Answer Chain
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    # Final Retrieval Chain
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    return rag_chain, llm


# ==============================================================================
# SESSION STATE INITIALIZATION
# ==============================================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "repo_processed" not in st.session_state:
    st.session_state.repo_processed = False

if "repo_stats" not in st.session_state:
    st.session_state.repo_stats = None


# ==============================================================================
# SIDEBAR: Repository Processing
# ==============================================================================

st.sidebar.title("🔧 Repository Configuration")
st.sidebar.markdown("---")

# GitHub URL Input
github_url = st.sidebar.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repo",
    help="Enter the full URL of a public GitHub repository to analyze",
)

# Process Button
if st.sidebar.button("🚀 Process Repository", type="primary", use_container_width=True):
    if not github_url:
        st.sidebar.error("⚠️ Please enter a GitHub URL")
    elif not github_url.startswith("https://github.com/"):
        st.sidebar.error("⚠️ Invalid GitHub URL format")
    else:
        # Clear existing ChromaDB
        if os.path.exists("./chroma_db"):
            with st.sidebar.status("🧹 Cleaning previous data..."):
                safe_rmtree("./chroma_db")
                st.session_state.repo_processed = False
                st.session_state.repo_stats = None
                st.session_state.messages = []
                st.session_state.chat_history = []

                # Force reload of RAG pipeline
                if "rag_chain" in st.session_state:
                    del st.session_state["rag_chain"]
                st.cache_resource.clear()

        # Process repository
        with st.sidebar.status("📥 Processing repository...", expanded=True) as status:
            try:
                st.write("📥 Downloading files from GitHub...")
                st.write("🔍 Analyzing code structure...")
                st.write("📊 Generating embeddings...")
                st.write("💾 Storing in vector database...")

                success, stats = process_repository(github_url)

                if success:
                    st.session_state.repo_processed = True
                    st.session_state.repo_stats = stats
                    # Add repo URL to stats if not present
                    if "repo_url" not in st.session_state.repo_stats:
                        st.session_state.repo_stats["repo_url"] = github_url
                    if "repo_name" not in st.session_state.repo_stats:
                        # Extract repo name from URL
                        repo_name = github_url.rstrip("/").split("/")[-1]
                        st.session_state.repo_stats["repo_name"] = repo_name

                    status.update(
                        label="✅ Repository processed successfully!", state="complete"
                    )
                    st.sidebar.success(f"Processed {stats['total_chunks']} code chunks")
                    st.sidebar.info(
                        "💡 Check the Repository Stats page for detailed analytics!"
                    )
                else:
                    status.update(label="❌ Processing failed", state="error")
                    st.sidebar.error(
                        "Failed to process repository. Check console for details."
                    )

            except Exception as e:
                st.sidebar.error(f"Error: {str(e)}")
                status.update(label="❌ Error occurred", state="error")

# Display Quick Stats in Sidebar
if st.session_state.repo_stats:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Quick Stats")
    stats = st.session_state.repo_stats

    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("📁 Files", stats.get("total_files", 0))
    with col2:
        st.metric("🧩 Chunks", stats.get("total_chunks", 0))

    st.sidebar.info("📊 View detailed stats in the **Repository Stats** page!")

# Navigation Tips
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
### 💡 Quick Tips
- 📚 New here? Check the **How to Use** page
- 📊 View detailed stats in **Repository Stats**
- 💬 Ask questions about code structure, logic, and more!

### 🎯 Example Questions
- "What is the overall architecture?"
- "How does authentication work?"
- "Explain the API endpoints"
- "What state management is used?"
"""
)

# Clear Chat Button
if st.session_state.repo_processed and st.session_state.messages:
    st.sidebar.markdown("---")
    if st.sidebar.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.rerun()


# ==============================================================================
# MAIN PANEL: Chat Interface
# ==============================================================================

st.title("💬 GitHub Repository Chatbot")
st.markdown(
    "Ask questions about the codebase using natural language. Powered by **Google Gemini 1.5 Flash**"
)
st.markdown("---")

# Check if repository has been processed
if not st.session_state.repo_processed:
    st.info("👈 **Start by processing a GitHub repository using the sidebar**")

    # Helpful information for new users
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
        ### 🚀 Getting Started
        
        1. **Enter a GitHub URL** in the sidebar
        2. **Click "Process Repository"** button
        3. **Wait** for ingestion to complete (1-5 minutes)
        4. **Start asking questions** about the code!
        
        The chatbot will analyze the entire codebase and answer questions based on actual code.
        """
        )

    with col2:
        st.markdown(
            """
        ### 🤖 How It Works
        
        This uses **RAG (Retrieval-Augmented Generation)**:
        
        1. 📝 Your question → Vector embedding
        2. 🔍 Search ChromaDB for similar code
        3. 📤 Retrieved code → Sent to Gemini
        4. 💡 AI generates answer based on context
        
        **Supports:** JavaScript, TypeScript, Python, Markdown, Images & more!
        """
        )

    st.markdown("---")
    st.info("💡 **First time?** Visit the **📚 How to Use** page for a complete guide!")

else:
    # Repository is processed - show chat interface

    # Display current repository
    if st.session_state.repo_stats and "repo_name" in st.session_state.repo_stats:
        st.success(
            f"✅ Currently analyzing: **{st.session_state.repo_stats['repo_name']}**"
        )

    # Load RAG pipeline (cached)
    if "rag_chain" not in st.session_state:
        with st.spinner("🔄 Loading AI models..."):
            rag_chain, llm = load_rag_pipeline()
            st.session_state.rag_chain = rag_chain
            st.session_state.llm = llm

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if user_query := st.chat_input(
        "Ask about the codebase (e.g., 'How does routing work?')"
    ):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching codebase and generating answer..."):
                try:
                    # Invoke RAG chain
                    response = st.session_state.rag_chain.invoke(
                        {
                            "input": user_query,
                            "chat_history": st.session_state.chat_history,
                        }
                    )

                    answer = response["answer"]

                    # Display answer
                    st.markdown(answer)

                    # Update chat history
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                    st.session_state.chat_history.append(
                        HumanMessage(content=user_query)
                    )
                    st.session_state.chat_history.append(AIMessage(content=answer))

                    # Display retrieved source chunks
                    with st.expander("📄 View Retrieved Code Chunks"):
                        for i, doc in enumerate(response["context"]):
                            st.markdown(
                                f"**Chunk {i+1}** | Source: `{doc.metadata.get('source', 'Unknown')}`"
                            )
                            st.code(doc.page_content, language="python")
                            st.markdown("---")

                except Exception as e:
                    st.error(f"❌ Error generating response: {str(e)}")
                    st.info(
                        "💡 Try rephrasing your question or check if the repository was processed correctly."
                    )

# Footer
st.markdown("---")
st.caption("Powered by Groq LLaMA 3.1-8B-Instant • ChromaDB • LangChain • Streamlit")
