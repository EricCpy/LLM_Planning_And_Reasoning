**Anecdotal Evaluation:**

1. [x] Bing AI Search (Copilot)
2. [x] Regular ChatGPT  
3. [x] ChatGPT Search Feature  
4. [x] AutoGPT
5. [x] Google Search -> scrape the first x pages -> parse to markdown -> use prompt with content of the first x pages -> output the top AI conferences as JSON, see if it can give the output in JSON format -> use JSON output for a new query, rank the conferences by search volume using Google Search Analytics  
    - [x] Llama 3.1 **hf_hub_download(repo_id="bartowski/Meta-Llama-3.1-8B-Instruct-GGUF", filename="Meta-Llama-3.1-8B-Instruct-Q6_K_L.gguf")**
    - [x] Llama 3.2 **hf_hub_download(repo_id="bartowski/Llama-3.2-3B-Instruct-GGUF", filename="Llama-3.2-3B-Instruct-Q6_K_L.gguf")** 
    - [x] Mini Nemotron **hf_hub_download(repo_id="bartowski/Mistral-NeMo-Minitron-8B-Instruct-GGUF", filename="Mistral-NeMo-Minitron-8B-Instruct-Q4_K_L.gguf")**
6. [x] Create a DB for RAG with the first x scraped pages of the conferences
   - [x] **Llama 3.2**
7. [ ] Automated PoG Approach -> let LLM generate subtasks and then use the output of the subtasks in a prompt with the question
        