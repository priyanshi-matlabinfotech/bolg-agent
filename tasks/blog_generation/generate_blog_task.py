from crewai import Task
from tasks.blog_generation.get_blogs_task import get_blogs_task
from agents.blog_generation.generate_blog_agent import generate_blog_agent


def generate_blog_task():
    return Task(
        description="""
            Create a comprehensive and user-friendly blog post on the topic of "{topic}" 
            using the content extracted from the blogs obtained in the previous task. Your goal is to:
            1. Analyze the gathered blog content for insights, best practices, and common structures.
            2. Synthesize this information to create a more cohesive, understandable, and informative blog post.
            3. Ensure the new blog post is logically organized, engaging, and accessible to beginners.
            4. Generate at least one relevant image that complements the text, making the blog post more visually 
               attractive and engaging.

            The final blog should stand out in terms of clarity, structure, depth of information, 
            and visual appeal, providing a superior learning experience compared to the individual blogs it was 
            based on.
            The blog should have a minimum length of 1700 words.
            Return the comprehensive and user-friendly blog post on {topic} along with the images as output.
        """,
        agent=generate_blog_agent(),
        expected_output="""
            A new blog post in Markdown format titled "{topic}" that is:
            - A blog with a minimum of 1700 words.
            - More understandable, cohesive, and informative than the individual blogs.
            - Well-organized, engaging, and suitable for beginners.
            - A synthesis of the best practices and insights from the analyzed content.
            - Visually attractive with at least one relevant image that enhances the reader's experience.
        """,
        context=[get_blogs_task()]
    )
