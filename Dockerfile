# Selects the official Python Docker image (python:3.11-slim) as the base.
FROM python:3.11-slim

# Defines the working directory in the container as /app.
WORKDIR /app

# Copies requirements.txt file into the current working directory (/app) inside the Docker container.
COPY requirements.txt .

# Installs the Python packages specified in requirements.txt inside the container.
RUN pip install --no-cache-dir -r requirements.txt

# Copies all project's files (e.g., main.py, other source code) from local directory into the container directory (/app).
COPY . .

# Tells Docker that the container will listen on port 8000.
EXPOSE 8000

# Specifies the command that will run when your Docker container starts.
# uvicorn is an ASGI server, ideal for running FastAPI applications.
# main:app tells uvicorn to find the app object in the Python file named main.py.
# --host 0.0.0.0 allows the app to accept connections from outside the container.
# --port 8000 sets the listening port.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# How to use the Dockerfile.
# 1. Build Docker image:
#       docker build -t openai-api-app .
# 2. Run Docker container:
#       docker run -p 8000:8000 -e OPENAI_API_KEY="your_actual_key_here" openai-api-app
# 3. Test the containerized app
#       curl -X POST "http://localhost:8000/generate" \
#       -H "Content-Type: application/json" \
#       -d '{"prompt":"Hello, Docker!"}'