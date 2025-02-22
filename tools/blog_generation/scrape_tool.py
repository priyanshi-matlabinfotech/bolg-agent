from crewai.tools import BaseTool
from langchain_community.document_loaders import AsyncHtmlLoader


class GetHTMLTool(BaseTool):
    name: str = "Get HTML from URL Tool"
    description: str = """
        This tool takes the list of HTML URLs and returns the list containing the dictionary containing the following 
        format:
        [{
            "url": "https://example.com",
            "html_content": "<html>...</html>"
        },
        {
            "url": "https://example.org",
            "html_content": "<html>...</html>"
        }]
    """

    def _run(self, urls: list | str) -> list:

        # Load the HTML content of the URLs
        loader = AsyncHtmlLoader(urls)
        docs = loader.load()

        # create a dictionary that will map the URL to its HTML content.
        html_content = []
        for doc in docs:
            doc_dict = doc.dict()
            url_html = {
                "url": doc_dict["metadata"]["source"],
                "html_content": doc_dict["page_content"]
            }
            html_content.append(url_html)

        return html_content
