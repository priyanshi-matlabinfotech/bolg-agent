from crewai import Task
from agents.blog_generation.get_blogs_agent import get_blogs_agent


def get_blogs_task():
    return Task(
        description="""
            Your goal is to find blogs on the topic "{topic}". 
            To achieve this, follow these steps:
            1. Use the DuckDuckGoSearchTool to search the web for relevant blogs.
            2. Scrape the content of the identified blogs.
            3. Extract the blog URLs, raw HTML content, and the meaningful blog content from the scraped data.

            Ensure the output is a well-structured JSON-like array containing:
            - Blog URLs: The direct URLs to the blog posts.
            - Raw HTML Content: The HTML structure of each blog page.
            - Scraped Blog Content: The main textual content of the blogs, cleaned and organized.
        """,
        agent=get_blogs_agent(),
        expected_output="""
            A structured JSON-like array containing the blog URLs, raw HTML content, and scraped blog content.
        """
    )
