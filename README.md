# 🤖 RAG GitHub Repository Chatbot

An intelligent code analysis chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions about any GitHub repository. Built with Python, Streamlit, LangChain, ChromaDB, and Google Gemini AI.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)](https://langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Quick Start](#-quick-start)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Tech Stack](#-tech-stack)
- [Usage Guide](#-usage-guide)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Features

### Core Capabilities
- **🔄 Dynamic Repository Ingestion**: Clone and analyze any public GitHub repository on-demand
- **🧠 Syntax-Aware Code Chunking**: Uses LangChain's `LanguageParser` with tree-sitter to respect code structure (functions, classes)
- **💬 Conversational Memory**: Maintains chat context for follow-up questions
- **⚡ Fast AI Inference**: Powered by Google Gemini 1.5 Flash with 1M token context
- **📊 Repository Analytics**: Displays tech stack, file counts, and processing stats
- **🎨 Modern UI**: Clean Streamlit interface with real-time status updates

### Supported File Types
- **Code**: `.js`, `.jsx`, `.ts`, `.tsx`, `.py`
- **Documentation**: `.md`, `.txt`
- **Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg` (indexed but not yet processed)

---

## 🎬 Demo

### Processing a Repository
1. Enter any GitHub repository URL
2. Click "Process Repository"
3. Wait for automatic ingestion and indexing
4. Start asking questions!

### Example Questions
- "What is the overall architecture of this project?"
- "How does authentication work?"
- "Explain the API endpoints"
- "What database is being used?"
- "Show me the component structure"

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+** installed
- **Git** installed
- **Google Gemini API Key** (free at [Google AI Studio](https://aistudio.google.com/apikey))

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rag-github-chatbot.git
cd rag-github-chatbot
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

**Expected time:** 3-5 minutes

#### 3. Configure API Key

Open `pages/3_💬_Chatbot.py` and update line 35:
```python
os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY_HERE"
```

**Get your free API key:**
1. Visit https://aistudio.google.com/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy and paste into the code

#### 4. Run the Application
```bash
streamlit run app.py
```

The app will automatically open at `http://localhost:8501`

---

## 🧠 How It Works

### RAG Pipeline Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                      USER INTERFACE                            │
│                   (Streamlit Web App)                          │
└────────────────────────┬───────────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────────┐
│                 INGESTION PIPELINE                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ GitHub   │─▶│ Language │─▶│ Sentence │─▶│ ChromaDB │      │
│  │ Clone    │  │ Parser   │  │ Embedder │  │ Storage  │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└────────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────────┐
│                 RAG RETRIEVAL CHAIN                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ User     │─▶│ Context  │─▶│ Vector   │─▶│ Gemini   │      │
│  │ Question │  │ Reformer │  │ Search   │  │ AI       │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└────────────────────────────────────────────────────────────────┘
```

### Step-by-Step Process

#### 1. **Repository Ingestion**
```python
# Clone GitHub repository
git clone https://github.com/user/repo → ./cloned_repo/

# Parse code files with syntax awareness
LanguageParser → respects functions, classes, logical blocks

# Generate embeddings (384-dimensional vectors)
HuggingFace all-MiniLM-L6-v2 → converts code to vectors

# Store in vector database
ChromaDB → enables semantic similarity search
```

#### 2. **Question Processing**
```python
# User asks: "How does authentication work?"

# Step 1: Reformulate with chat history context
LangChain History-Aware Retriever → standalone question

# Step 2: Convert to embedding vector
all-MiniLM-L6-v2 → 384-dim vector

# Step 3: Search vector database
ChromaDB similarity search → retrieve top 6 relevant code chunks

# Step 4: Generate answer with context
Google Gemini 1.5 Flash → coherent explanation with code references
```

---

## 📁 Project Structure

```
rag-github-chatbot/
│
├── app.py                          # Main Streamlit application entry point
├── ingest.py                       # Repository ingestion and processing logic
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
├── rag_evaluation_metrics.ipynb    # Jupyter notebook for RAG evaluation
│
├── pages/                          # Streamlit multi-page app
│   ├── 1_📊_Repository_Stats.py   # Analytics and statistics page
│   ├── 2_📚_How_to_Use.py         # User guide and instructions
│   └── 3_💬_Chatbot.py            # Main chatbot interface
│
├── .streamlit/               # Streamlit configuration (auto-generated)
│   └── config.toml
│
├── chroma_db/                # Vector database storage (auto-generated)
│   ├── chroma.sqlite3        # Metadata and document storage
│   └── [collection-id]/      # HNSW vector indices
│
├── cloned_repo/              # Temporary GitHub clone directory (auto-generated)
└── __pycache__/              # Python cache (auto-generated)
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Landing page with project overview and navigation |
| `ingest.py` | Handles GitHub cloning, code parsing, embedding generation, and ChromaDB storage |
| `pages/3_💬_Chatbot.py` | Core RAG pipeline with LangChain chains and Gemini integration |
| `pages/1_📊_Repository_Stats.py` | Visualizes repository analytics and tech stack |
| `pages/2_📚_How_to_Use.py` | Interactive user guide |
| `rag_evaluation_metrics.ipynb` | Jupyter notebook for evaluating RAG performance (Precision, Recall, MRR) |

---

## ⚙️ Configuration

### Embedding Model Configuration
```python
# ingest.py
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",  # Fast, 384-dim embeddings
    model_kwargs={"device": "cpu"},  # CPU-only (no GPU required)
    encode_kwargs={"normalize_embeddings": True}  # L2 normalization
)
```

### Chunking Parameters
```python
# ingest.py
CHUNK_SIZE = 1000      # Characters per chunk (~250 tokens)
CHUNK_OVERLAP = 200    # Overlap to prevent mid-function splits
```

### Retrieval Configuration
```python
# pages/3_💬_Chatbot.py
retriever = vectorstore.as_retriever(
    search_type="similarity",  # Cosine similarity search
    search_kwargs={"k": 6}     # Retrieve top 6 most relevant chunks
)
```

### Gemini Model Configuration
```python
# pages/3_💬_Chatbot.py
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",  # Fast and efficient
    temperature=0.2,                  # Low randomness for accuracy
    max_output_tokens=8192            # Long-form responses
)
```

---

## 🛠️ Tech Stack

### Core Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **UI Framework** | Streamlit 1.30+ | Modern web interface with chat components |
| **RAG Orchestration** | LangChain 0.1+ | Chains, retrievers, document processing |
| **Vector Database** | ChromaDB | HNSW-based similarity search |
| **Embeddings** | HuggingFace all-MiniLM-L6-v2 | 384-dim sentence embeddings |
| **LLM** | Google Gemini 1.5 Flash | Fast inference with 1M token context |
| **Code Parsing** | LangChain LanguageParser + tree-sitter | Syntax-aware code chunking |
| **Git Operations** | GitPython | Repository cloning |

### Why These Choices?

#### **Gemini 1.5 Flash vs Alternatives**
| Model | Context Window | Speed | Cost | Quality |
|-------|----------------|-------|------|---------|
| **Gemini 1.5 Flash** | 1M tokens | ⚡⚡⚡⚡⚡ | Free tier | ⭐⭐⭐⭐ |
| GPT-4 Turbo | 128K tokens | ⚡⚡⚡ | $0.01/1K | ⭐⭐⭐⭐⭐ |
| Claude 3.5 Sonnet | 200K tokens | ⚡⚡⚡⚡ | $0.003/1K | ⭐⭐⭐⭐⭐ |
| Llama 3.1 8B (Groq) | 8K tokens | ⚡⚡⚡⚡⚡ | Free | ⭐⭐⭐ |

**Decision:** Gemini offers the best balance of context window (crucial for code), speed, and free availability.

#### **ChromaDB vs Alternatives**
| Vector DB | Setup | Performance | Features |
|-----------|-------|-------------|----------|
| **ChromaDB** | Local, zero-config | Fast HNSW | Built-in persistence |
| Pinecone | Cloud, API keys | Very fast | Managed service |
| Weaviate | Docker required | Very fast | Advanced filtering |
| FAISS | Local, CPU/GPU | Fastest | No metadata |

**Decision:** ChromaDB requires zero setup and provides excellent performance for local deployments.

---

## 📚 Usage Guide

### First-Time Setup

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Navigate to the Chatbot page** (sidebar)

3. **Process a repository:**
   - Enter GitHub URL: `https://github.com/username/repository`
   - Click "🚀 Process Repository"
   - Wait 1-5 minutes (depends on repo size)

4. **Start asking questions!**

### Best Practices

#### ✅ Good Questions
- "Explain the authentication flow"
- "What database models are defined?"
- "How are API routes structured?"
- "What styling framework is used?"

#### ❌ Avoid
- Questions about code execution (the bot reads, doesn't run)
- Questions requiring external documentation
- Questions about deployment (unless in code comments)

### Tips for Better Results

1. **Be Specific**: Instead of "How does this work?", ask "How does user login validation work?"
2. **Reference Components**: "Explain the AuthContext component"
3. **Ask Follow-ups**: The bot remembers conversation context
4. **Check Sources**: File paths are mentioned in responses

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **ModuleNotFoundError: No module named 'langchain_google_genai'**
```bash
pip install langchain-google-genai
```

#### 2. **404 Error: models/gemini-1.5-flash is not found**
**Solution:** Update model name in `pages/3_💬_Chatbot.py`:
```python
model="gemini-1.5-flash-latest"  # or "gemini-pro"
```

#### 3. **Rate Limit Exceeded / 413 Request Too Large**
**Cause:** Token limit exceeded (old Groq setup)  
**Solution:** Already fixed! Using Gemini now with 1M token context.

#### 4. **ChromaDB Permission Error (Windows)**
**Cause:** Git marks files as read-only  
**Solution:** Already handled in `ingest.py` with `remove_readonly()` function

#### 5. **Empty Responses / No Context Retrieved**
**Cause:** Repository not processed correctly  
**Solution:**
- Click "🚀 Process Repository" again
- Check console for error messages
- Ensure GitHub URL is public

#### 6. **API Key Error**
**Solution:**
1. Get key from https://aistudio.google.com/apikey
2. Update in `pages/3_💬_Chatbot.py` line 35
3. Restart Streamlit

---

## 🎓 How RAG Works (Educational)

### What is RAG?

**RAG (Retrieval-Augmented Generation)** combines:
1. **Retrieval**: Finding relevant information from a knowledge base
2. **Generation**: Using an LLM to generate coherent answers

### Why RAG Instead of Just LLMs?

| Approach | Knowledge Freshness | Hallucination Risk | Cost |
|----------|---------------------|-------------------|------|
| **Pure LLM** | Training cutoff only | High | High (large prompts) |
| **RAG** | Always current | Low (grounded in facts) | Low (targeted context) |

### The RAG Process Explained

```
User Question: "How does login work?"
                    ↓
1. EMBEDDING
   "How does login work?" → [0.23, -0.45, 0.89, ...]
                    ↓
2. SIMILARITY SEARCH
   ChromaDB finds similar code chunks:
   - auth.js (similarity: 0.92)
   - login.jsx (similarity: 0.89)
   - routes.js (similarity: 0.85)
                    ↓
3. CONTEXT ASSEMBLY
   Relevant code → Combined into prompt context
                    ↓
4. LLM GENERATION
   Gemini reads context + question → Generates explanation
                    ↓
   Answer: "Login is handled by the AuthContext..."
```

---

## 🌟 Advanced Features

### Conversational Memory

The chatbot remembers conversation history:

```
You: "What frontend framework is used?"
Bot: "The project uses React with React Router..."

You: "What state management does it use?"
Bot: "It uses React Context API, as mentioned before..."
       ↑ Remembers previous context
```

### Syntax-Aware Chunking

Unlike naive text splitting, this system uses **tree-sitter** to parse code:

```python
# Bad (naive splitting):
"function login(user) {\n  if (user.p"  # Split mid-function!

# Good (syntax-aware):
"function login(user) {\n  if (user.password) {\n    authenticate();\n  }\n}"
```

---

## 📈 Performance Metrics

### Typical Processing Times

| Repository Size | Files | Processing Time | Chunks Generated |
|----------------|-------|-----------------|------------------|
| Small (< 50 files) | 30-50 | 30-60 sec | 100-300 |
| Medium (50-200 files) | 100-200 | 2-4 min | 500-1500 |
| Large (200+ files) | 300+ | 5-10 min | 2000+ |

### Query Response Times

- **Embedding generation**: ~50ms
- **Vector search**: ~100ms
- **Gemini inference**: ~1-3 seconds
- **Total response time**: ~2-4 seconds

---

## 📊 RAG System Evaluation

### Evaluation Metrics Jupyter Notebook

This project includes a comprehensive evaluation notebook (`rag_evaluation_metrics.ipynb`) that measures the RAG system's performance using standard information retrieval metrics.

#### Metrics Calculated

1. **Precision**: Proportion of retrieved documents that are relevant
   - Formula: `Relevant Retrieved / Total Retrieved`
   - Tells you: "How accurate are my results?"

2. **Recall**: Proportion of relevant documents that were retrieved
   - Formula: `Relevant Retrieved / Total Relevant`
   - Tells you: "Am I finding all the relevant information?"

3. **MRR (Mean Reciprocal Rank)**: Average rank of the first relevant document
   - Formula: `1/|Q| × Σ(1/rank_i)`
   - Tells you: "How highly are relevant docs ranked?"

4. **F1-Score**: Harmonic mean of Precision and Recall
   - Formula: `2 × (Precision × Recall) / (Precision + Recall)`
   - Tells you: "What's the overall balance?"

#### Running the Evaluation

1. **Install Jupyter dependencies:**
   ```bash
   pip install jupyter pandas matplotlib seaborn numpy
   ```

2. **Process a repository first:**
   ```bash
   streamlit run app.py
   # Process a GitHub repository to create chroma_db/
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook rag_evaluation_metrics.ipynb
   ```

4. **Run all cells** to see:
   - Detailed metrics for each test query
   - Visualizations (bar charts, line plots, heatmaps)
   - Recommendations for improvement
   - Exported CSV results

#### Customizing the Evaluation

Modify the `test_dataset` in the notebook to match your repository:

```python
test_dataset = [
    {
        "query": "authentication login",
        "relevant_keywords": ["auth", "login", "password"],
        "relevant_files": ["auth", "login"],
        "description": "Should retrieve auth-related code"
    },
    # Add more test cases...
]
```

#### Typical Results

| Metric | Poor | Fair | Good | Excellent |
|--------|------|------|------|-----------| 
| Precision | <0.4 | 0.4-0.6 | 0.6-0.8 | >0.8 |
| Recall | <0.4 | 0.4-0.6 | 0.6-0.8 | >0.8 |
| MRR | <0.4 | 0.4-0.6 | 0.6-0.8 | >0.8 |
| F1-Score | <0.4 | 0.4-0.6 | 0.6-0.8 | >0.8 |

#### Improvement Strategies

Based on evaluation results, the notebook provides automated recommendations:
- **Low Precision**: Improve chunking or use better embeddings
- **Low Recall**: Increase retrieval k or expand queries
- **Low MRR**: Implement re-ranking with cross-encoders
- **Low F1**: Use hybrid search (semantic + keyword)

---

## 🤝 Contributing

Contributions are welcome! Here are some areas for improvement:

### Enhancement Ideas
- [ ] Add support for more programming languages (Java, Go, Rust)
- [ ] Implement actual image analysis with vision models
- [ ] Add code execution sandbox
- [ ] Export chat history as markdown
- [ ] Multi-repository analysis (compare codebases)
- [ ] Code quality metrics integration
- [ ] Real-time GitHub webhook updates

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LangChain** for the excellent RAG framework
- **Google** for free Gemini API access
- **ChromaDB** for the simple yet powerful vector database
- **Streamlit** for making beautiful ML apps easy
- **HuggingFace** for open-source embedding models

---

## 📞 Support

Having issues? Here's how to get help:

1. **Check the [Troubleshooting](#-troubleshooting) section**
2. **Search existing GitHub Issues**
3. **Create a new issue with:**
   - Error message
   - Python version
   - Steps to reproduce

---

## 🔮 Future Roadmap

- ✅ Google Gemini integration (DONE)
- ✅ Syntax-aware code parsing (DONE)
- ✅ Conversational memory (DONE)
- ⏳ Vision AI for architecture diagrams
- ⏳ Multi-language support (Java, C++, Go)
- ⏳ Code quality analysis integration
- ⏳ Automated PR review assistant
- ⏳ Export functionality (PDF reports)

---

<div align="center">

**Built with ❤️ using Python, LangChain, and AI**

[⭐ Star this repo](https://github.com/yourusername/rag-github-chatbot) if you find it useful!

</div>
