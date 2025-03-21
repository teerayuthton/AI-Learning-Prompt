# How to create API Key and call with OpenAI API

Before we call with OpenAI API,
We need to create API Key.

1. Go to https://platform.openai.com/ then Sign Up.
2. Continue the flows, The OpenAI will asking you to create First API Key.
3. Setup Key name then tap on "Generate API Key".
![Screenshot 2568-03-21 at 14 14 26](https://github.com/user-attachments/assets/eb6ac0d0-32a0-4a87-b44e-859f4d4e9cce)

4. Then successful create API Key.
5. You need to install library openai using `pip install openai` on your terminal.
6. Then create some python file and copy+paste the code that provided from OpenAI then run python script.
![Screenshot 2568-03-21 at 14 15 18](https://github.com/user-attachments/assets/57f9ee45-d1f5-4176-96b3-90403f1c19e6)

That is the result when we updated the command.

This line calls OpenAI's API using the `client.chat.completions.create` method.

Parameters:

  `model="gpt-4o-mini"` → Specifies which GPT model to use.

  `messages=[{"role":"user", "content":prompt}]`
    
  Sends a list of messages to the model.
    
  The message has:
      
  `"role": "user"` → Marks the message as coming from a user.
      
  `"content": prompt` → The actual user input.
  
  `max_tokens=100` → Limits the response to 100 tokens (words & symbols combined).

![Screenshot 2568-03-21 at 15 58 50](https://github.com/user-attachments/assets/f89e9891-9fe3-4273-b9bf-57c8bab23be5)
