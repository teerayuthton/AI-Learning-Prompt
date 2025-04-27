# How Chain of though work?

![Screenshot 2568-04-10 at 10 42 08](https://github.com/user-attachments/assets/3104f45e-9bb0-4527-9c73-206ad650e3ef)


## First we have to reuse function `get_response` from package `simple_call`

![Screenshot 2568-04-10 at 10 43 32](https://github.com/user-attachments/assets/4ddf9b18-2e01-4a7a-bc19-d474cbf47869)

We need to append path '../' back to upper path for access to package `simple_call`

![Screenshot 2568-04-10 at 10 45 44](https://github.com/user-attachments/assets/948e3c4d-544a-497d-951b-80b03b1b2498)


![Screenshot 2568-04-10 at 10 45 01](https://github.com/user-attachments/assets/880db7eb-3d4e-41c0-b362-a7ce7e2f7794)

Then we created file `__init__.py` under finder `simple_call` for make this directory as a package `simple_call`
Inside of `__init__.py` we will import function `get_response` for let anothers python script can call function `get_response`
When that script import package `simple_call`

![Screenshot 2568-04-10 at 10 45 22](https://github.com/user-attachments/assets/31dce9a6-ffb4-4348-9cf0-4c699c58d199)


## Chain-of-Thought (CoT)

Definition: A Chain-of-Thought (CoT) prompt is a prompting technique designed to encourage large language models to generate intermediate reasoning steps before arriving at a final answer. Instead of simply providing the answer, the model is guided to think step-by-step, which often leads to more accurate and reliable results, especially for complex or multi-step problems.
When to use:
- Math Problems: Solving multi-step arithmetic or algebra problems.
- Logic Puzzles: Reasoning through logical or verbal puzzles.
- Coding: Debugging or writing algorithms.
- Explanations: Providing clear and structured reasoning for complex topics.

Result is
```
Let's break down the problem step by step.

1. **Determine the current age of the friend:**
   - Your friend is currently 20 years old.

2. **Calculate the current age of the friend's father:**
   - According to the problem, the father is currently double the age of the friend.
   - So, we calculate the father's age: 
     [
     text{Father's age} = 2 times text{Friend's age} = 2 times 20 = 40
     ]

3. **Find the age of the father in 10 years:**
   - To find the father's age in 10 years, we simply add 10 years to his current age:
     [
     text{Father's age in 10 years} = text{Current father's age} + 10 = 40 + 10 = 50
     ]

4. **Conclusion:**
   - In 10 years, your friend's father will be **50 years old**.
```
