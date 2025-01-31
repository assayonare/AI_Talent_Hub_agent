import aiohttp
import asyncio
import pytest

pytest_plugins = "pytest_asyncio" 
API_URL = "http://127.0.0.1:8000/api/request"

# Функция для отправки запроса к API
async def send_request(session, query, query_id):
    json_data = {"query": query, "id": query_id}
    
    async with session.post(API_URL, json=json_data) as response:
        assert response.status == 200  # Проверяем, что статус 200 OK
        result = await response.json()
        assert "id" in result
        assert "answer" in result
        assert "reasoning" in result
        assert "sources" in result
        print(f"Запрос {query_id} -> Ответ API:", result)
        return result

# Основная тестовая функция
@pytest.mark.asyncio
async def test_api():
    queries = [
        ("В каком году был основан Университет ИТМО?\n1. 1900\n2. 1909\n3. 1915\n4. 1920", 1),
        ("Где находится главный кампус Университета ИТМО?\n1. Москва\n2. Санкт-Петербург\n3. Екатеринбург\n4. Нижний Новгород", 2),
        ("Сколько факультетов у Университета ИТМО?", 3),
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, query, i) for i, (query, i) in enumerate(queries)]
        results = await asyncio.gather(*tasks)

        assert len(results) == len(queries)  # Проверяем, что ответы пришли на все запросы

if __name__ == "__main__":
    asyncio.run(test_api())