FROM python:3.10

WORKDIR /blog_agent

#copy current dir content into the container at /blog_agent
COPY ./requirements.txt /blog_agent/requirements.txt

#install requirements.txt
RUN pip install --no-cache-dir --upgrade -r /blog_agent/requirements.txt


# set up a new user named "user" with ID 1000
RUN useradd -m -u 1000 user

#switch to "user" user
USER user

# Set home to the user's home directory
ENV HOME=/home/user 
ENV PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app
 
# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

## Start the FastAPI app on port 7860, the default port expected by Spaces
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
