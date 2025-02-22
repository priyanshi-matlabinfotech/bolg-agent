from typing import Any
from duckduckgo_search import DDGS
from crewai.tools import BaseTool


class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search tool"
    description: str = """
        DuckDuckGoSearchTool is a web-based tool designed to streamline your search for relevant blog content across the
        internet. By simply entering a query, DuckDuckGoSearchTool intelligently scans the web to identify and return 
        URLs of blogs that match your topic of interest.
    """

    def _run(self, query: Any) -> Any:
        final_query = f"intitle:{query}, inurl:blog"
        results = DDGS().text(final_query, max_results=5)
        result_urls = []
        for result in results:
            result_urls.append(result['href'])

        return result_urls
