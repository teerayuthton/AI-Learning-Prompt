from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from openai import OpenAI
import httpx
import logging

# Configures logging to show messages with INFO.
logging.basicConfig(level=logging.INFO)

# Creates a logger instance for the current script/module.
logger = logging.getLogger(__name__)

# Initializes a new FastAPI instance to build a RESTful API.
app = FastAPI()

# Securely get your API key from environment variable.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(
    api_key=OPENAI_API_KEY,
    http_client=httpx.Client(verify=False),
)

# Defines a simple data model for the request body using Pydantic.
class PromptRequest(BaseModel):
    prompt: str

# Decorator telling FastAPI that the endpoint /generate will accept HTTP POST requests.
@app.post("/generate")
async def generate_response(request: PromptRequest): # Defines an asynchronous Python function named.
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": request.prompt}],
            max_tokens=100
        )
        result = response.choices[0].message.content
        # Logs the input prompt and generated response for monitoring and debugging purposes.
        logger.info(f"Prompt: {request.prompt} | Response: {result}")
        return {"response": result}
    except Exception as e:
        # Logs the error details to help debug the issue.
        logger.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")