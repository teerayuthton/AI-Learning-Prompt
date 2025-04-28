# How to run App locally using FastAPI

![Screenshot 2568-04-28 at 21 50 29](https://github.com/user-attachments/assets/c9fdbd0b-cc7b-4e6e-8625-06c6253810f2)

## Import required Frameworks

![Screenshot 2568-04-28 at 21 55 37](https://github.com/user-attachments/assets/77275a27-3611-472f-8771-75e1ebffb817)

- Imports FastAPI, a modern, high-performance Python web framework, and HTTPException for handling errors gracefully in API responses.
- Imports BaseModel from Pydantic, used for data validation and serialization of API inputs.
- Imports the built-in Python module os for accessing environment variables.
- Imports the official OpenAI client to interact with OpenAI services and models.
- Imports httpx, a modern HTTP client used internally by the OpenAI client.
- Imports the Python built-in logging module for tracking application behavior and issues.

![Screenshot 2568-04-28 at 22 00 09](https://github.com/user-attachments/assets/0d5ac116-401e-408c-ac62-fcc90c353707)

- Configures logging to show messages with INFO level and higher.
- Creates a logger instance for the current script/module.

![Screenshot 2568-04-28 at 22 01 08](https://github.com/user-attachments/assets/d518b6f8-29b3-4bf2-b3f9-caee8d85f5da)

- Initializes a new FastAPI instance to build a RESTful API.

![Screenshot 2568-04-28 at 22 02 15](https://github.com/user-attachments/assets/82bc2dce-3b9c-477f-b4ec-a501cc141898)

- Retrieves your OpenAI API key from the operating system environment variable named OPENAI_API_KEY.
- Checks if the API key is present. If not set, it raises an error prompting you to provide it securely.
- Creates an instance of OpenAI’s API client.
- Passes your API key securely.
- Uses httpx.Client with verify=False to skip SSL verification, 
useful in some network environments (but generally not recommended for production unless necessary).

![Screenshot 2568-04-28 at 22 04 04](https://github.com/user-attachments/assets/fccceb24-a587-44c9-a4bf-3cbf2da911eb)

- Defines a simple data model (PromptRequest) with one required field, prompt, of type string.
- FastAPI uses this model to automatically parse and validate incoming JSON request bodies.

![Screenshot 2568-04-28 at 22 05 12](https://github.com/user-attachments/assets/1a2a7a87-8f1d-41e3-9333-553068d353b4)

- Decorator telling FastAPI that the endpoint /generate will accept HTTP POST requests.
- Defines an asynchronous Python function named generate_response which takes one argument (request) matching the PromptRequest data model.

![Screenshot 2568-04-28 at 22 06 46](https://github.com/user-attachments/assets/5dc0348a-4987-4f27-bd5f-f4ec09e22732)

- Catches any exceptions that occur during the API call or processing.
- Logs the error details to help debug the issue.
- Sends a standardized error response to the user with HTTP status code 500 (Internal Server Error).

## How to run API Locally

1. Go to project directory of main.py
2. Run `uvicorn main:app --host 0.0.0.0 --port 8000`
You should see

![Screenshot 2568-04-28 at 22 11 33](https://github.com/user-attachments/assets/8a4b4703-4641-43c3-a8cb-025a4ecaf494)

### Open another terminal then run
```
curl -X POST "http://localhost:8000/generate" \
-H "Content-Type: application/json" \
-d '{"prompt":"Tell me about AI."}'
```
You will get response 
```
{"response":
"Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that typically
require human intelligence. These tasks include understanding natural language,
recognizing patterns, solving problems, learning from experience,
and making decisions. AI can be categorized into several key areas:\n\n1.
**Types of AI**:\n   - **Narrow AI**: Also known as Weak AI, it is designed for specific tasks,
such as virtual assistants (like Siri or Alexa), recommendation systems (like Netflix or Amazon), and"}%
```



