import re
from app.search import search_web
from app.news import get_latest_news
from app.deepseek import get_together_answer

def process_query(query: str, query_id: int):
    # Проверяем, есть ли варианты ответов
    options = re.findall(r"\n?(\d+)\.\s(.*?)\n?", query)
    
    if "новости" in query.lower() and "итмо" in query.lower():
        answer = None
        
        reasoning, sources = get_latest_news()
        
    elif options:
        answer, reasoning = get_together_answer(query)
        sources = search_web(query)

    else:
        answer = None
        reasoning = get_together_answer(query)
        sources = search_web(query)

    return {
        "id": query_id,
        "answer": answer,
        "reasoning": reasoning,
        "sources": sources
    }