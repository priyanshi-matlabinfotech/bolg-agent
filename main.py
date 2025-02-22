import os
import traceback
import logging

from crewai import Crew
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,Any


from agents.blog_generation.generate_blog_agent import generate_blog_agent
from agents.blog_generation.get_blogs_agent import get_blogs_agent
from tasks.blog_generation.get_blogs_task import get_blogs_task
from tasks.blog_generation.generate_blog_task import generate_blog_task


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()



class BlogInput(BaseModel):
    query: str
    filename: Optional[Any] = Field(None,description="filename of the markdown file.")

class BlogCrew:
    def __init__(self,query):
        self.query = query

    def run(self):
        inputs = self.query
        crew = Crew(
            agents=[get_blogs_agent(),get_blogs_agent()],
            tasks=[get_blogs_task(),generate_blog_task()],
            verbose=True,
            inputs=inputs
            )

        result = crew.kickoff()

        return result.raw


@app.post("/generate_blog")
def generate_blog_agent(req: BlogInput):

    try:
        logger.info(f"query: {req.query}")
        crew = BlogCrew(req.query)
        result = crew.run()

        if req.filename is None:
            filename= f"{req.query.lower().replace('', '_')}.md"
        else:
            if req.filename.endswith(".md"):
                filename = req.filename
            else:
                filename = f"{req.filename}.md"

        os.makedirs('output',exist_ok=True)

        with open(f'output/{filename}','w') as f:
            f.write(result)

        logger.info(f"blog successfully created in file: {filename}")
        return {'blog': result}
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})