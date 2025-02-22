import os
import traceback

from crewai import Crew
from flask import Flask, jsonify,request

from agents.blog_generation.get_blogs_agent import get_blogs_agent
from agents.blog_generation.generate_blog_agent import generate_blog_agent
from tasks.blog_generation.generate_blog_task import generate_blog_task
from tasks.blog_generation.get_blogs_task import get_blogs_task

app = Flask(__name__)

class BlogCrew:
    def __init__(self,query):
        self.query = query

    def run(self):
        inputs = self.query
        crew = Crew(
            agents=[get_blogs_agent(),generate_blog_agent()],
            tasks=[get_blogs_task(),generate_blog_task()],
            verbose=True,
            inputs=inputs
            )

        result = crew.kickoff()

        return result.raw



@app.route("/")
def home():
    return  jsonify({"msg":"hello"})


@app.route("/blog_generator",methods=['POST'])
def blog_generator_fn():
    data = request.get_json()
    query = data.get('query')
    filename = data.get('filename')

    try:
        blog_crew=BlogCrew(query)
        result=blog_crew.run()

        if filename:
            if filename.endswith('.md'):
                filename = filename
            else:
                filename = f"{filename}.md"
        else:
            filename = f"{query.lower().replace(' ','_')}.md"

        os.makedirs("output",exist_ok=True)

        with open(f"output/{filename}",'w') as f:
            f.write(result)

        return {'blog': result}

    except Exception as e:
        traceback.print_exc()
        return jsonify(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=8000)