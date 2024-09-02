from typing import Any

from httpx import AsyncClient


async def search_books(book_name: str) -> dict[str, Any]:

    url = f"/search.json?q={book_name.replace(' ','+')}"
    aclient = AsyncClient(base_url="https://openlibrary.org")
    response = await aclient.get(url)
    response_body: dict[str, Any] = response.json()

    return response_body
