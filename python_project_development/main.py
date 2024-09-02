import asyncio

from python_project_development.books import search_books


async def main() -> None:
    result = await search_books("The Hobbit")

    print("Found:", result.get("numFound", 0), "\n")

    for doc in result.get("docs", []):
        print("Title:", doc.get("title", ""))


if __name__ == "__main__":

    asyncio.run(main())
