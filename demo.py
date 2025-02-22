import os
import traceback
from typing import Any, Optional
from crewai import Crew
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from agents.blog_generation.get_blogs_agent import get_blogs_agent
from agents.blog_generation.generate_blog_agent import generate_blog_agent
from tasks.blog_generation.get_blogs_task import get_blogs_task
from tasks.blog_generation.generate_blog_task import generate_blog_task


load_dotenv()
app = FastAPI(
    title="Blog Generator",
    description="Generate a new blog based on the topic provided."
)


class GenerateBlogInput(BaseModel):
    query: str
    filename: Optional[Any] = Field(None, description="filename of the markdown file.")


class BlogCrew:

    def __init__(self, query):
        self.query = query

    def run(self):

        agent_get_blogs = get_blogs_agent()
        agent_generate_blog = generate_blog_agent()

        task_get_blogs = get_blogs_task()
        task_generate_blog = generate_blog_task()
        inputs = self.query
        crew = Crew(
            agents=[agent_get_blogs, agent_generate_blog],
            tasks=[task_get_blogs, task_generate_blog],
            verbose=True,

        )

        result = crew.kickoff(inputs = inputs)
        return result.raw


@app.post("/api/blog_generator")
def generate_blog(req: GenerateBlogInput):
    try:
        blog_crew = BlogCrew(req.query)
        result = blog_crew.run()

        # save result into a markdown file
        if req.filename is not None:
            if req.filename.endswith(".md"):
                filename = req.filename
            else:
                filename = f"{req.filename}.md"
        else:
            filename = f"{req.query.lower().replace(' ', '_')}.md"

        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", filename), "w") as f:
            f.write(result)

        print(f"blog saved into output/{filename}")
        return {"blog": result}
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})


