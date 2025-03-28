# How Chain of though work?

![Screenshot 2568-03-27 at 16 21 16](https://github.com/user-attachments/assets/6dd32653-a817-4683-9e63-5b882c8e3608)

## First we have to reuse function `get_response` from file `simple_call`

![Screenshot 2568-03-26 at 17 11 50](https://github.com/user-attachments/assets/a6b72ba1-2571-4ecb-aa53-8517141c3a73)

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
