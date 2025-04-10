# What is Zero/One/Few shot prompt?

![Screenshot 2568-04-10 at 10 54 49](https://github.com/user-attachments/assets/b3d81f81-f4aa-4b9b-b284-a8be45ef8a78)

## First we have to reuse function `get_response` from package `simple_call`

![Screenshot 2568-04-10 at 10 43 32](https://github.com/user-attachments/assets/4ddf9b18-2e01-4a7a-bc19-d474cbf47869)

We need to append path '../' back to upper path for access to package `simple_call`

![Screenshot 2568-04-10 at 10 45 44](https://github.com/user-attachments/assets/948e3c4d-544a-497d-951b-80b03b1b2498)

![Screenshot 2568-04-10 at 10 56 30](https://github.com/user-attachments/assets/f66cc012-6e1f-4bad-9bad-389af375d7fc)


Then we created file `__init__.py` under finder `simple_call` for make this directory as a package `simple_call`
Inside of `__init__.py` we will import function `get_response` for let anothers python script can call function `get_response`
When that script import package `simple_call`

![Screenshot 2568-04-10 at 10 45 22](https://github.com/user-attachments/assets/31dce9a6-ffb4-4348-9cf0-4c699c58d199)

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

