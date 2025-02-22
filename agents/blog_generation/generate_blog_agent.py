from crewai import Agent
from dotenv import load_dotenv
from utils.llm import get_ollama

load_dotenv()


def generate_blog_agent():
    return Agent(
        role="Content Analyst and Creator",
        backstory="""
            You excel at transforming complex or fragmented information into clear, cohesive, and highly 
            informative content. Your expertise lies in synthesizing key insights into a single, well-structured 
            blog that stands on its own, without referencing the sources it was derived from. Your focus is on 
            crafting content that is not only understandable and engaging but also appears as an original and 
            standalone piece of writing.
        """,
        goal="""            
            Generate a new blog post using llm, drawing on the insights extracted from provided content. The new 
            blog post should be a standalone piece that does not reference the original sources. It should be more 
            understandable, cohesive, and informative, while presenting the information in an engaging and 
            accessible way. You can use the image generator tool to create images that complement the text and 
            enhance the visual appeal of the blog post. The output should be a blog that is more readable, 
            informative, and visually attractive than typical blog posts, with generated images from relevant 
            prompts to illustrate key points. The generated blog should be in Markdown format and should not 
            mention the previous blogs. Return the generated blog with images as your Final Answer.
        """,
        allow_delegation=False,
        verbose=True,
        max_iter=50,

        llm=get_ollama()
    )
