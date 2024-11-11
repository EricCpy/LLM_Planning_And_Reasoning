import requests
from bs4 import BeautifulSoup
import markdownify
from llama_cpp import Llama
from llama_cpp import LogitsProcessorList
from lmformatenforcer import CharacterLevelParser
from lmformatenforcer.integrations.llamacpp import build_llamacpp_logits_processor
from typing import Optional
from pydantic import BaseModel, Field
from lmformatenforcer import JsonSchemaParser

class Queries(BaseModel):
    queries: list[str] = Field(description="Google Search Query for Topic")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def get_top_urls_for_google_search_query(query: str, number: int = 5) -> list[dict]:
    url = f"https://www.google.com/search?q={query}"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results_div = soup.find("div", id="rso") # list of urls inside this elem
    if not results_div:
        print("FAILED BECAUSE GOOGLE SEARCH OUTPUT CHANGED!")
        return []
    
    output = []
    for a_tag in results_div.find_all("a", href=True):
        title_tag = a_tag.find("h3")
        if title_tag:
            title = title_tag.get_text()
            url = a_tag['href']
            output.append({"title": title, "url": url})
            if len(output) >= number:
                break

    return output

def scrape_and_convert_to_markdown(urls: list[str]) -> list[str]:
    markdown_texts = []
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            markdown_text = markdownify.markdownify(str(soup))
            markdown_texts.append(markdown_text)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue

    return markdown_texts

def llamacpp_with_character_level_parser(llm: Llama, prompt: str, character_level_parser: Optional[CharacterLevelParser]) -> str:
    logits_processors: Optional[LogitsProcessorList] = None
    if character_level_parser:
        logits_processors = LogitsProcessorList([build_llamacpp_logits_processor(llm, character_level_parser)])
    
    output = llm(prompt, logits_processor=logits_processors, max_tokens=4096)
    text: str = output['choices'][0]['text']
    return text

def llm_generate_search_queries(llm: Llama, prompt: str) -> list[str]:
    prompt = f"{prompt}\nYou MUST answer using the following json schema: {Queries.model_json_schema()}"
    queries = llamacpp_with_character_level_parser(llm, prompt, JsonSchemaParser(Queries.model_json_schema()))
    queries = Queries.model_validate_json(queries).queries
    return queries