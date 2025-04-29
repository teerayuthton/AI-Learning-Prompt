# How to create Unit testing

![Screenshot 2568-04-29 at 17 47 50](https://github.com/user-attachments/assets/7bc173d9-1b88-45e9-9885-57eebfc73f0a)

## Import

![Screenshot 2568-04-29 at 17 51 05](https://github.com/user-attachments/assets/284f3ad5-b470-41ec-ace1-74acb817655a)

- Imports the pytest testing framework, which helps you structure tests, make assertions, and report results.
- Imports TestClient from FastAPI, a testing utility to simulate HTTP requests against your FastAPI app.
- Imports patch from Python’s unittest.mock, allowing you to mock or replace parts of your code during tests.
- Imports your FastAPI app object (app) from your application module (src/main.py).
- This lets the test client perform HTTP requests directly against the running app.

## Initializing the Test Client

![Screenshot 2568-04-29 at 17 52 58](https://github.com/user-attachments/assets/ec32859d-35c7-4747-8683-6e00b82936e8)

## First Test case (Success case)

![Screenshot 2568-04-29 at 17 53 35](https://github.com/user-attachments/assets/6004fb39-5a7b-4b08-b76e-ced5a3998fb1)

- Uses patch to replace the real OpenAI API call (client.chat.completions.create) with a mock function during this test.
- This prevents actual external calls to OpenAI, ensuring your tests run quickly and reliably.

![Screenshot 2568-04-29 at 17 56 45](https://github.com/user-attachments/assets/b7eb4cec-f304-4c78-885b-9d24a58f5149)

- Configures the mocked OpenAI response to return a predefined structure:
- Mimics the response shape you expect from the real OpenAI API.
- Creates an object dynamically with the desired properties (a message with "content").

## Second Test case (Failed case)

![Screenshot 2568-04-29 at 17 58 09](https://github.com/user-attachments/assets/fc5fb9ba-19b9-4f1e-b01d-aa322284b67c)

- Similar setup as before, but designed to simulate an error scenario from OpenAI’s API.
- Confirms your app correctly returns an HTTP 500 Internal Server Error when encountering an unexpected issue.
- Checks that your app returns the standard error message format you defined in your exception handling logic.

## Third Test case (Invalid Request Data)

![Screenshot 2568-04-29 at 18 00 33](https://github.com/user-attachments/assets/0dc6b31e-2ffb-44c3-b9aa-c52cf702156c)

- Tests how your app responds when receiving invalid or missing data.
- Sends an empty JSON object ({}) instead of the required "prompt" field, intentionally causing a validation error.
- Verifies that FastAPI correctly identifies the invalid input and returns HTTP status code 422 Unprocessable Entity,
indicating a validation error from your input schema (PromptRequest model).

# How to run Unit test

On terminal run bash command
```
pytest tests/ --cov=src --cov-report=xml
```

## Result is

![Screenshot 2568-04-29 at 18 04 22](https://github.com/user-attachments/assets/5dd3a9a7-7d9e-4b3d-95e2-741c166d98e5)


