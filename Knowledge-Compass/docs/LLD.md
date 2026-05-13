# Low Level Design (LLD)

## 1. API Layer
**Endpoints**
- `POST /query` → Main interface for user queries
- `POST /ingest` → Upload SOPs / PDFs / ticket data
- `POST /feedback` → Capture user feedback
- `GET /health` → System health check

**Responsibilities**
- Entry point for client interactions
- Input validation, authentication, RBAC
- Stateless design for horizontal scaling
- Error handling with meaningful messages and fallback


## 2. Agentic Layer
**Components**
- `planner.py` → Intent analysis, ReAct workflow
- `orchestrator.py` → Parallel agent execution, aggregation
- `doc_agent.py` → Document retrieval, ACL filtering
- `ticket_agent.py` → Ticket retrieval, hybrid search
- `summarizer.py` → Merge results, remove redundancy

**Workflow**
User Query → Planner → Orchestrator → (Document Agent + Ticket Agent) → Summarizer → Output Context



## 3. Retrieval Layer
**Components**
- `embedding_service.py` → Text → vector embeddings
- `vector_search.py` → Semantic similarity search
- `bm25_search.py` → Keyword search
- `hybrid_retriever.py` → Combine vector + keyword
- `mmr_filter.py` → Remove duplicates
- `reranker.py` → Improve ranking precision

**Workflow**
Query → Embedding → Vector Search + BM25 → Hybrid Retriever → MMR Filter → Reranker → Final Results


## 4. LLM & Decision Layer
**Components**
- `llm_generator.py` → Generate responses using context
- `judge_agent.py` → Validate responses, detect hallucinations
- `decision_engine.py` → Respond / Clarify / Escalate

**Flow**
Retrieved Context → LLM Generator → Draft Response → Judge Agent → Confidence Score → Decision Engine → Final Output


## 4. Data Layer
**Technologies**
- PostgreSQL → Structured data
- pgvector → Vector similarity search
- MinIO → Raw file storage

**Tables**
- `documents` → SOP content, metadata, ACL
- `tickets` → Incident details
- `embeddings` → Vector representations


## 5. Data Processing Layer
**Components**
- `parser.py` → Extract text
- `cleaner.py` → Normalize data
- `chunker.py` → Split into chunks
- `embedding_pipeline.py` → Generate + store embeddings

**Workflow**
Raw File → Parser → Cleaner → Chunker → Embedding Pipeline → Storage


## 6. Ingestion Layer
**API-Based Ingestion**
- `ingestion_api.py` → Accept uploads
- `ingestion_service.py` → Parser → Chunker → Embedding pipeline

**Batch Ingestion**
- `batch_ingestion.py` → Bulk ingestion
- `data_loader.py` → Load files
- `scheduler.py` → Optional scheduled ingestion


## 7. Execution Flow
User → `/query` API → Planner → Orchestrator → Agents → Retrieval → Summarizer → LLM → Judge → Decision Engine → Response/Escalation


## 8. Inter-Layer Interaction
- **API → Agentic**: Validation, routing
- **Agentic → Retrieval**: Query data sources
- **Retrieval → Agentic**: Return filtered results
- **Agentic → LLM**: Summarized context
- **LLM → Decision**: Response + confidence
- **Decision → API**: Final output

**Ingestion Flow**
Batch/API → Ingestion Layer → Processing Layer → Data Layer



## 9. Design Benefits
- Clear separation of concerns
- Loose coupling for independent scaling
- Maintainability and extensibility
- Smooth data flow across layers
