# How to create API Key and call with OpenAI API

Before we call with OpenAI API,
We need to create API Key.

1. Go to https://platform.openai.com/ then Sign Up.
2. Continue the flows, The OpenAI will asking you to create First API Key.
3. Setup Key name then tap on "Generate API Key".
![Screenshot 2568-03-21 at 14 14 26](https://github.com/user-attachments/assets/5a4d3a6e-8fd3-42ed-8f31-9d9950985abf)


4. Then successful create API Key.
5. You need to install library openai using `pip install openai` on your terminal.
6. Then create some python file and copy+paste the code that provided from OpenAI then run python script.
![Screenshot 2568-03-21 at 14 15 18](https://github.com/user-attachments/assets/7a3a8ea0-5d3c-4ad4-b12c-cbd51c4d01dd)

# Here this is sample prompt for call OpenAI API

![Screenshot 2568-03-21 at 21 51 04](https://github.com/user-attachments/assets/6a1bd1ee-c1c5-4ebf-9fd3-f9ac8530f134)

This line calls OpenAI's API using the `client.chat.completions.create` method.

Parameters:

  `model="gpt-4o-mini"` → Specifies which GPT model to use.

  `messages=[{"role":"user", "content":prompt}]`
    
  Sends a list of messages to the model.
    
  The message has:
      
  `"role": "user"` → Marks the message as coming from a user.
      
  `"content": prompt` → The actual user input.
  
  `max_tokens=100` → Limits the response to 100 tokens (words & symbols combined).

