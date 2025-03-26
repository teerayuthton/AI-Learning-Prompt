# What is Zero/One/Few shot prompt?

![Screenshot 2568-03-26 at 17 10 04](https://github.com/user-attachments/assets/e1747925-bd6f-4ee6-a89f-b78567460bdc)

## First we have to reuse function `get_response` from file `simple_call`

![Screenshot 2568-03-26 at 17 11 50](https://github.com/user-attachments/assets/a6b72ba1-2571-4ecb-aa53-8517141c3a73)

### Zero-shot prompt

Definition: The model is given a task without any examples.
When to Use:
- When the task is simple or well-known.
- For general knowledge questions or straightforward requests.

![Screenshot 2568-03-26 at 17 13 05](https://github.com/user-attachments/assets/8a845770-cfb5-409c-9b5c-f036b1b214b1)

Result is
```
Zero shot is:  Bonjour.
```

### One-shot prompt

Definition: The model is given one example before performing the task.
When to Use:
- When the task is a bit complex.
- If the model needs a small hint to understand the context.

![Screenshot 2568-03-26 at 17 13 57](https://github.com/user-attachments/assets/37c5ad3f-5fba-40c7-8c3c-7c9e664dffce)

Result is
```
One shot is:  Merci.
```

### Few-shot prompt

Definition: The model is given one example before performing the task.
When to Use:
- When the task is more complex or requires nuance.
- For tasks requiring a specific style or tone.

![Screenshot 2568-03-26 at 17 17 45](https://github.com/user-attachments/assets/6f3cf118-a471-451d-86dc-c0dcde8ce096)

Result is
```
Few shot is:  À plus tard.
```

