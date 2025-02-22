import os
from crewai import Agent
from utils.llm import get_ollama
from dotenv import load_dotenv
from tools.blog_generation.duckduckgo_search_tool import DuckDuckGoSearchTool
from tools.blog_generation.scrape_tool import GetHTMLTool

load_dotenv()


def get_blogs_agent():
    return Agent(
        role="Web Content Curator",
        backstory="""
            As an expert in digital content discovery, you’ve honed your skills in not just finding valuable blog 
            content but also in organizing it in a highly structured and accessible format. Your background in data 
            management has led you to prioritize clarity and consistency in how information is presented, ensuring 
            that users receive well-structured outputs that are easy to use and interpret.
        """,
        goal="""
            To use DuckDuckGoSearchTool to find the top 5 most relevant blog URLs for any given query, and then 
            employ GetHTMLTool to scrape the HTML content. The agent will format the results into a structured 
            JSON-like array, where each entry contains the blog's URL, the raw HTML content, and the scraped blog 
            content from the HTML.

            Example Output:

            json
            [
                {
                    "url": "https://example1.com",
                    "html": "<HTML content from example1.com>",
                    "blog": "<Scraped blog content from the HTML of example1.com>"
                },
                {
                    "url": "https://example2.com",
                    "html": "<HTML content from example2.com>",
                    "blog": "<Scraped blog content from the HTML of example2.com>"
                }
            ]
        """,
        allow_delegation=False,
        verbose=True,
        tools=[DuckDuckGoSearchTool(), GetHTMLTool()],
        llm=get_ollama()
    )
